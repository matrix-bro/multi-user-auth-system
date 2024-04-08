from django.urls import path
from app import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('super/dashboard/', views.super_dashboard, name='super_dashboard'),
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),
]
