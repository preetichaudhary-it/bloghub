from django.urls import path
from .views import home,profile,about,contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('profile/', profile, name='profile')
]