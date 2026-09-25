from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, BlogPostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BlogPost, Category
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    latest_blogs = BlogPost.objects.order_by(
        '-created_at'
    )[:4]

    categories = Category.objects.all()

    context = {
        'latest_blogs': latest_blogs,
        'categories': categories
    }

    return render(
        request,
        'home.html',
        context
    )

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        print("Register form submitted")
        form = RegisterForm(request.POST)

        if form.is_valid():
            print("Form valid")
            form.save()

            messages.success(request, "Account created successfully.")
            return redirect('login') 
        else:
            print(form.errors)

    else:
        form = RegisterForm()

    return render(request, 'register.html',{'form':form})

def login_view(request):
    if request.user.is_authenticated:
            return redirect('home')

    # Default values for validation messages
    username_error = None
    password_error = None
    login_error = None

    # Keep username after an unsuccessful submission
    username = ''

    if request.method == 'POST':
        username = request.POST.get('username', '').strip() # get values from html
        password = request.POST.get('password', '')

        # Username validation
        if not username:
            username_error = "Username is required."

        # Password validation
        if not password:
            password_error = "Password is required"

        # Authentication 
        if not username_error and not password_error:
            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome Back, {user.username}!")
                return redirect('home')

            else:
                login_error = "Invalid username or password."

    return render(
        request,
        'login.html',
        {
            'username': username,
            'username_error': username_error,
            'password_error': password_error,
            'login_error': login_error,
        }
    )

@login_required
def profile(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)

    messages.success(request, "You have been logged out successfully.")
    return redirect('home')

@login_required
def create_blog(request):

    if request.method == 'POST':

        form = BlogPostForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            blog = form.save(commit=False)

            blog.author = request.user

            blog.save()

            messages.success(
                request,
                "Blog created successfully."
            )

            return redirect('blog-list')

    else:

        form = BlogPostForm()

    return render(
        request,
        'blog/create_blog.html',
        {
            'form': form
        }
    )

def blog_list(request):

    blog_posts = BlogPost.objects.all().order_by('-created_at')

    paginator = Paginator(blog_posts, 6)

    page_number = request.GET.get('page')

    blogs = paginator.get_page(page_number)

    return render(
        request,
        'blog/blog_list.html',
        {
            'blogs': blogs
        }
    )

def blog_detail(request, blog_id):

    blog = get_object_or_404(
        BlogPost,
        id=blog_id
    )

    return render(
        request,
        'blog/blog_detail.html',
        {
            'blog': blog
        }
    )

@login_required
def edit_blog(request, pk):

    blog = get_object_or_404(
        BlogPost,
        pk=pk
    )

    if request.user != blog.author:
        return redirect('blog-detail', blog_id=blog.id)

    if request.method == 'POST':

        form = BlogPostForm(
            request.POST,
            request.FILES,
            instance=blog
        )

        if form.is_valid():
            form.save()

            return redirect(
                'blog-detail',
                blog_id=blog.id
            )

    else:

        form = BlogPostForm(
            instance=blog
        )

    context = {
        'form': form,
        'blog': blog
    }

    return render(
        request,
        'blog/edit_blog.html',
        context
    )

@login_required
def delete_blog(request, pk):

    blog = get_object_or_404(
        BlogPost,
        pk=pk
    )
     # Only author can delete
    if request.user != blog.author:
        return redirect(
            'blog-detail',
            blog_id=blog.id
        )

    if request.method == 'POST':

        blog.delete()

        return redirect(
            'blog-list'
        )

    return redirect(
        'blog-detail',
        blog_id=blog.id
    )
