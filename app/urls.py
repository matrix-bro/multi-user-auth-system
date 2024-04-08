from django.urls import path
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('super/dashboard/', views.super_dashboard, name='super_dashboard'),
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),
]
