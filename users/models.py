from django.db import models
from django.contrib.auth.models import AbstractUser
import random, string
from django.utils import timezone
from decimal import Decimal


class Country(models.Model):
    name_en = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_uz = models.CharField(max_length=100)

    def __str__(self):
        return self.name_en


class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategories(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    banner = models.ImageField(upload_to='company_banners/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    owner = models.OneToOneField('User', on_delete=models.CASCADE, related_name='company', null=True, blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    telephone = models.CharField(max_length=50, null=True, blank=True)
    # email = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", default="static/default-logo.svg")
    trust = models.BooleanField(default=False)
    company_name = models.CharField(max_length=100, blank=True,
                                    null=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name="user_category")
    subcategories = models.ManyToManyField(SubCategories, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    telegram = models.CharField(max_length=100, blank=True, null=True)
    whatsapp = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=500, blank=True, null=True)
    url_maps = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    is_business_account = models.BooleanField(default=None, blank=True, null=True)
    currency = models.DecimalField(max_digits=10, decimal_places=3, default=100.000)
    previous_currency = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    is_phone_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def calculate_average_rating(self):
        return UserRating.objects.filter(rated_user=self).aggregate(models.Avg("rating"))["rating__avg"] or 0

    def save(self, *args, **kwargs):
        if self.pk:
            self.previous_currency = self._get_previous_value("currency", self.currency)
        super().save(*args, **kwargs)

    def _get_previous_value(self, field_name, current_value):
        if self.pk:
            previous_instance = self.__class__._default_manager.get(pk=self.pk)
            previous_value = getattr(previous_instance, field_name)

            # Преобразуем оба значения в Decimal
            return Decimal(previous_value) if previous_value is not None else Decimal(current_value)
        return Decimal(current_value)


class OTPCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otp_codes')
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()  # Время истечения срока действия кода
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"OTP code for {self.user.username} - {self.code}"

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(random.choices(string.digits, k=6))
        self.expires_at = timezone.now() + timezone.timedelta(minutes=10)  # Код будет действовать 10 минут
        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() > self.expires_at

    def can_be_used(self):
        """Проверка, можно ли использовать код"""
        return not self.is_used and not self.is_expired()


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    recipients = models.ManyToManyField(User, related_name="received_messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        recipients_str = ", ".join(str(user) for user in self.recipients.all())
        return f"Message from {self.sender} to {recipients_str}: {self.message}"


class UserRating(models.Model):
    rater = models.ForeignKey(User, related_name="ratings_given", on_delete=models.CASCADE)
    rated_user = models.ForeignKey(User, related_name="ratings_received", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

    class Meta:
        unique_together = (("rater", "rated_user"),)

    def __str__(self):
        return f"Rating from {self.rater} to {self.rated_user}: {self.rating}"


class UserSubscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriptions")
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscribers")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("subscriber", "target_user")

    def __str__(self):
        return f"{self.subscriber} подписан на {self.target_user}"


class Complaint(models.Model):
    COMPLAINT_CHOICES = [
        ("spam", "Спам"),
        ("inappropriate_content", "Неуместный контент"),
        ("harassment", "Домогательство"),
    ]

    complaint_type = models.CharField(max_length=50, choices=COMPLAINT_CHOICES, verbose_name="Тип жалобы")
    description = models.TextField(verbose_name="Описание проблемы")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_complaints",
                               verbose_name="Отправитель")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_complaints",
                                  verbose_name="Получатель")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.complaint_type} - {self.sender.username} to {self.recipient.username} - {self.created_at}"


class PointsTransaction(models.Model):
    TRANSACTION_TYPES = (
        ("purchase", "Purchase"),
        ("usage", "Usage"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.amount}"


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


@receiver(post_save, sender=get_user_model())
def update_currency_transaction(sender, instance, created, **kwargs):
    if not created:
        previous_currency = Decimal(instance.previous_currency)
        current_currency = Decimal(instance.currency)

        PointsTransaction.objects.create(
            user=instance,
            transaction_type="purchase" if current_currency > previous_currency else "usage",
            amount=abs(current_currency - previous_currency),
        )
