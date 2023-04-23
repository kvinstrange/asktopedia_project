from django import views
from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('userregister/',UserRegisterview.as_view(),name='userregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('dashboard/',DashBoardView.as_view(),name='dashboard'),
    path('user/dashboard/',UserDashBoardView.as_view(),name='user_dashboard'),
    path('userprofile/',UserProfileView.as_view(),name='user_profile'),

]