from django import views
from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('userregister/',UserRegisterview.as_view(),name='userregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('dashboard/',DashBoardView.as_view(),name='dashboard'),
    path('user/dashboard/',UserDashBoardView.as_view(),name='user_dashboard'),
    path('userprofile/<int:pk>',UserProfileView.as_view(),name='user_profile'),
    path('userupdate/<int:pk>',UserUpdateView.as_view(),name='user_update'),
    # Password Reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]