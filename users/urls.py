from django.urls import path
from .views import RegisterViewSet, UpdateUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('user/register', RegisterViewSet.as_view(), name='register'),
    path('user/<int:id>/', UpdateUserView.as_view(), name='update-user'),
    path('login', TokenObtainPairView.as_view(), name='obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),
]
