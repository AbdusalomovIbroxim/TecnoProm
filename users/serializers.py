from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import PointsTransaction
from rest_framework.validators import UniqueValidator

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    telephone = serializers.CharField(max_length=15)  # Телефон
    password = serializers.CharField(write_only=True)  # Пароль

    # telephone = serializers.CharField(max_length=50)
    # password = serializers.CharField(write_only=True)

    # def validate(self, data):
    #     telephone = data.get("telephone")
    #     password = data.get("password")
    #
    #     try:
    #         user = User.objects.get(telephone=telephone)
    #     except User.DoesNotExist:
    #         raise serializers.ValidationError("Пользователь с таким номером телефона не найден.")
    #
    #     # Проверяем правильность пароля
    #     if not user.check_password(password):
    #         raise serializers.ValidationError("Неверный пароль.")
    #
    #     return data


class RegisterSerializer(serializers.ModelSerializer):
    telephone = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(write_only=True, min_length=8)
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        required=True,
    )

    class Meta:
        model = User
        fields = ("id", "telephone", "password", "username")

    def create(self, validated_data):
        user = User.objects.create_user(
            telephone=validated_data["telephone"],
            password=validated_data["password"],
            username=validated_data["username"],
        )
        user.is_phone_verified = False
        user.save()
        return user


class VerifyPhoneSerializer(serializers.Serializer):
    telephone = serializers.CharField()
    code = serializers.CharField(max_length=6)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "telephone",
            "is_business_account",
            "currency",
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "description", "profile_photo")


class AddPointsSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=1)
