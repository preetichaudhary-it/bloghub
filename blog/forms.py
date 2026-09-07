from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username.isdigit():
            raise forms.ValidationError("Username cannot contain only numbers.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter username'
        })

        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter email address'
        })
        
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter password'
        })
        
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm password'
        })
