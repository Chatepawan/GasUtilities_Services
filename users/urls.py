# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # Add other user-related URLs here if needed, such as login, logout, etc.
]
