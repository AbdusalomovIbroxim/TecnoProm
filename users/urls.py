from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (MeView, RegisterView, UserListView,
                    UserDetailView, UserUpdateView, 
                    AddPointsToUserView, 
                    )

urlpatterns = [
    # path('auth/me', MeView.as_view(), name='me'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/', UserListView.as_view(), name='user_list'),

    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),

    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),

    path('user/add-points/', AddPointsToUserView.as_view(), name='add_points_to_user')
]
