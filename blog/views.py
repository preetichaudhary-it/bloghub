from django.shortcuts import render, redirect
from .forms import RegisterForm
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

@login_required
def profile(request):
    return render(request, 'profile.html')