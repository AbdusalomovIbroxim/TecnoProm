import uuid

from django.contrib.auth import get_user_model
from django.db.models import (
    Model,
    CharField,
    SlugField,
    CASCADE,
    ForeignKey,
    DateTimeField,
    BooleanField,
    PositiveBigIntegerField,
    ImageField,
    SET_NULL,
    ManyToManyField,
    PositiveIntegerField,
    FloatField,
)
from django.urls import reverse_lazy
from django.utils.translation import get_language


class Categories(Model):
    slug = SlugField(unique=True)
    name_en = CharField("Category (English)", max_length=50, default="")
    name_ru = CharField("Категория (Русский)", max_length=50, default="")
    name_uz = CharField("Kategoriya (O'zbek)", max_length=50, default="")
    is_linked = BooleanField(default=False)

    def __str__(self):
        language_code = get_language()
        return {
            'uz': self.name_uz,
            'ru': self.name_ru,
            'en': self.name_en,
        }.get(language_code, self.name_en)

    def get_absolute_url(self):
        return reverse_lazy("category_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SubCategories(Model):
    slug = SlugField(unique=True)
    name_en = CharField("Subcategory (English)", max_length=100, default="")
    name_ru = CharField("Подкатегория (Русский)", max_length=100, default="")
    name_uz = CharField("Subkategoriya (O'zbek)", max_length=100, default="")
    is_linked = BooleanField(default=False)

    def __str__(self):
        language_code = get_language()
        return {
            'uz': self.name_uz,
            'ru': self.name_ru,
            'en': self.name_en,
        }.get(language_code, self.name_en)

    def get_absolute_url(self):
        return reverse_lazy("subcategory_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"


class SubCategoryCategory(Model):
    subcategory = ForeignKey(SubCategories, on_delete=CASCADE)
    category = ForeignKey(Categories, on_delete=CASCADE)


class Tag(Model):
    name_en = CharField("Tag Name (English)", max_length=255, unique=True, default="")
    name_ru = CharField("Имя тега (Русский)", max_length=255, unique=True, default="")
    name_uz = CharField("Tag nomi (O'zbek)", max_length=255, unique=True, default="")
    is_linked = BooleanField(default=False)

    def __str__(self):
        language_code = get_language()
        return {
            'uz': self.name_uz,
            'ru': self.name_ru,
            'en': self.name_en,
        }.get(language_code, self.name_en)


class TagCategory(Model):
    category = ForeignKey(Categories, on_delete=CASCADE, related_name="tags")
    tag = ForeignKey(Tag, on_delete=CASCADE, related_name="category_tags")


class TagSubcategory(Model):
    subcategory = ForeignKey(SubCategories, on_delete=CASCADE, related_name="tags")
    tag = ForeignKey(Tag, on_delete=CASCADE, related_name="subcategory_tags")


class Country(Model):
    slug = SlugField(unique=True)
    name_en = CharField("Country (English)", max_length=50, default="")
    name_ru = CharField("Страна (Русский)", max_length=50, default="")
    name_uz = CharField("Davlat (O'zbek)", max_length=50, default="")

    def __str__(self):
        language_code = get_language()
        return {
            'en': self.name_en,
            'ru': self.name_ru,
            'uz': self.name_uz,
        }.get(language_code, self.name_uz)

    def get_absolute_url(self):
        language_code = get_language()
        urls = {
            'en': "country_detail",
            'ru': "country_detail_ru",
            'uz': "country_detail_uz",
        }
        return reverse_lazy(urls.get(language_code, "country_detail"), kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class City(Model):
    slug = SlugField(unique=True)
    country = ForeignKey(Country, on_delete=CASCADE)
    name_en = CharField("Country (English)", max_length=50, default="")
    name_ru = CharField("Страна (Русский)", max_length=50, default="")
    name_uz = CharField("Davlat (O'zbek)", max_length=50, default="")

    def __str__(self):
        language_code = get_language()
        return {
            'uz': self.name_uz,
            'ru': self.name_ru,
            'en': self.name_en,
        }.get(language_code, self.name_en)

    def get_absolute_url(self):
        language_code = get_language()
        urls = {
            'en': "country_detail",
            'ru': "country_detail_ru",
            'uz': "country_detail_uz",
        }
        return reverse_lazy(urls.get(language_code, "country_detail"), kwargs={"slug": self.slug})

    class Meta:
        ...
        # verbose_name = "Город"
        # verbose_name_plural = "Города"


class Products(Model):
    TYPE_CHOICES = [
        ("buy", "Buy"),
        ("sell", "Sell"),
    ]
    slug = SlugField(unique=True, blank=True)
    title = CharField("Наименование", max_length=100)
    description = CharField("Описание", max_length=900, null=True, blank=True)
    telephone = CharField("Номер телефона", max_length=30)
    telephone_view_count = PositiveBigIntegerField("Количество просмотров номер телефона", default=0)
    telegram = CharField("Телеграмм номер", max_length=100, blank=True, null=True)
    view_count = PositiveBigIntegerField("Количество просмотров", default=0)
    create_date = DateTimeField("Дата создания", auto_now_add=True)
    update_date = DateTimeField("Дата обновления", auto_now=True)
    is_published = BooleanField("Опубликовано", default=True)
    country = ForeignKey(Country, on_delete=CASCADE)
    city = ForeignKey(City, on_delete=CASCADE, blank=True, null=True)
    category = ForeignKey(Categories, on_delete=CASCADE)
    subcategories = ManyToManyField(SubCategories, blank=True)
    tags = ManyToManyField(Tag, blank=True)
    is_active = BooleanField(default=False)
    type = CharField(max_length=50, choices=TYPE_CHOICES, default="buy")
    author = ForeignKey(get_user_model(), on_delete=SET_NULL, blank=True, null=True)
    price = FloatField("Цена", blank=True, null=True)
    is_price_negotiable = BooleanField("Договорная цена", default=False)
    is_top_film = BooleanField(default=False)
    top_duration = PositiveIntegerField("Продолжительность в топе (в днях)", default=0)
    create_date_changed = BooleanField(default=False, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(uuid.uuid4())
        self.is_top_film = self.top_duration > 0

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("product-detail", kwargs={"slug": self.slug})

    class Meta:
        ...
        # verbose_name = "Запрос"
        # verbose_name_plural = "Запросы"


class Image(Model):
    image = ImageField(upload_to='product-image', default='product-image/default.jpg')
    product = ForeignKey("Products", on_delete=CASCADE)


class Favorite(Model):
    user = ForeignKey(get_user_model(), on_delete=CASCADE)
    product_id = ForeignKey(Products, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product_id")

    def __str__(self):
        return f"{self.user}, {self.product_id}"
