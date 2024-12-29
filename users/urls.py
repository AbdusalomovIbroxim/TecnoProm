from django.urls import path
from .views import (LoginView, RegisterView, MeView, VerifyPhoneView,
                    UserDetailView, UserDetailViewTelephone, UserUpdateView,
                    AddPointsView, )
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/me/', MeView.as_view(), name='me'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('auth/verify-phone/', VerifyPhoneView.as_view(), name='verify-phone'),
    path('users/<int:user_id>/', UserDetailView.as_view(), name='users-detail'),
    path('users/<str:telephone>/', UserDetailViewTelephone.as_view(), name='users-detail'),
    path('users/<int:user_id>/update/', UserUpdateView.as_view(), name='users-update'),
    path('users/<int:user_id>/add-points/', AddPointsView.as_view(), name='add-points'),
]
