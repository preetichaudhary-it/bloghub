from django.urls import path
from .views import (home, about, contact, register_view, login_view, logout_view, create_blog, blog_list, blog_detail,edit_blog, delete_blog, category_blogs, profile, edit_profile)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create-blog/', create_blog, name='create-blog'),
    path('blogs/', blog_list, name='blog-list'),
    path('blog/<int:blog_id>/', blog_detail, name='blog-detail'),
    path('blog/<int:pk>/edit/', edit_blog, name='edit-blog'),
    path('blog/<int:pk>/delete/', delete_blog, name='delete-blog'),
    path('category/<int:category_id>/', category_blogs, name='category-blogs'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),
]