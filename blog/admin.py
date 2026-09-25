from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BlogUser

# Registering models here.
@admin.register(BlogUser)
class BlogUserAdmin(UserAdmin):
    pass
