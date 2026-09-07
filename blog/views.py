from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

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