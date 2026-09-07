from django.urls import path
from .views import (home, about, contact, register_view, profile)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('register/', register_view, name='register'),
    path('profile/', profile, name='profile')
]