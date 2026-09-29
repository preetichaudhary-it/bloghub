from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BlogUser, Category, BlogPost, Contact, Feedback


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

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'created_at'
    )

    search_fields = (
        'name',
        'email',
        'subject'
    )

    ordering = (
        '-created_at',
    )

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'created_at'
    )

    search_fields = (
        'user__username',
    )

    ordering = (
        '-created_at',
    )