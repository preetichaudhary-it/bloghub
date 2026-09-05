from django.urls import path
from .views import home,profile,about

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('profile/', profile, name='profile')
]