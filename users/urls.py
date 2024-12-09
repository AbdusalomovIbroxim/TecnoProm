from django.urls import path
from .views import LoginView, RegisterView, VerifyPhoneView, UserDetailView, UserDetailViewTelephone, UserUpdateView, AddPointsView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('users/register/', RegisterView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('users/verify-phone/', VerifyPhoneView.as_view(), name='verify-phone'),
    path('user/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<str:telephone>/', UserDetailViewTelephone.as_view(), name='user-detail'),
    path('user/<int:user_id>/update/', UserUpdateView.as_view(), name='user-update'),
    path('user/<int:user_id>/add-points/', AddPointsView.as_view(), name='add-points'),
]
