from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from .models import OTPCode, PointsTransaction
from .serializers import (
    LoginSerializer,
    RegisterSerializer,
    VerifyPhoneSerializer,
    UserDetailSerializer,
    UserUpdateSerializer,
    AddPointsSerializer,
)
from django.contrib.auth import authenticate

User = get_user_model()


def authenticate_by_telephone(telephone, password):
    try:
        user = User.objects.get(telephone=telephone)
        if user.check_password(password):
            return user
        return None
    except User.DoesNotExist:
        return None


class LoginView(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            telephone = serializer.validated_data['telephone']
            password = serializer.validated_data['password']

            # Проверьте пользователя по телефону
            user = authenticate_by_telephone(telephone, password)
            if user is not None:
                OTPCode.objects.create(user=user)
                return Response({"message": "Вход успешен, OTP отправлен на ваш телефон."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Неверные учетные данные."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            OTPCode.objects.create(user=user)
            return Response({"message": "Пользователь зарегистрирован. Подтвердите номер телефона для продолжения."},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyPhoneView(APIView):
    @swagger_auto_schema(request_body=VerifyPhoneSerializer)
    def post(self, request):
        serializer = VerifyPhoneSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(telephone=serializer.validated_data["telephone"])
                otp = OTPCode.objects.filter(user=user, code=serializer.validated_data["code"]).first()

                if otp:
                    if otp.is_used:
                        return Response({"error": "Этот OTP код уже использован."}, status=status.HTTP_400_BAD_REQUEST)
                    if otp.is_expired():
                        return Response({"error": "Этот OTP код истёк."}, status=status.HTTP_400_BAD_REQUEST)

                    # Если код валидный
                    user.is_phone_verified = True
                    user.save()

                    otp.is_used = True
                    otp.save()

                    # Создание и возврат токенов
                    refresh = RefreshToken.for_user(user)
                    access_token = str(refresh.access_token)

                    return Response({
                        "message": "Телефон успешно подтвержден.",
                        "access_token": access_token,
                        "refresh_token": str(refresh)
                    })
                return Response({"error": "Неверный OTP."}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({"error": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: UserDetailSerializer})
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = UserDetailSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)


class UserDetailViewTelephone(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: UserDetailSerializer})
    def get(self, request, telephone):
        try:
            user = User.objects.get(telephone=telephone)
            serializer = UserDetailSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)


class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=UserUpdateSerializer)
    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            if request.user != user:
                return Response({"error": "Вы можете обновлять только свои данные."}, status=status.HTTP_403_FORBIDDEN)

            serializer = UserUpdateSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Данные пользователя успешно обновлены."})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)


class AddPointsView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=AddPointsSerializer)
    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = AddPointsSerializer(data=request.data)
            if serializer.is_valid():
                amount = serializer.validated_data["amount"]
                user.currency += amount
                user.save()

                PointsTransaction.objects.create(
                    user=user, transaction_type="purchase", amount=amount
                )
                return Response({"message": f"Добавлено {amount} баллов пользователю {user.username}."})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)
