from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BlogUser, Category, BlogPost


# Registering models here.
@admin.register(BlogUser)
class BlogUserAdmin(UserAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'category',
        'author',
        'created_at'
    ]