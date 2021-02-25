# -*- coding: utf-8 -*-

from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import CreateUserView

urlpatterns = [
    path('auth', jwt_views.TokenObtainPairView.as_view(), name='get_token'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('create', CreateUserView.as_view(), name='create_user'),
]
