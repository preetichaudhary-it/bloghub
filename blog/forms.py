from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BlogUser, BlogPost, Contact, Feedback
from django.utils.html import strip_tags

# =================== Register Form ========================
class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True
    )

    class Meta:
        model = BlogUser
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
        if BlogUser.objects.filter(email=email).exists():
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


# =================== BlogPost Form ========================
class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost

        fields = [
            'title',
            'category',
            'image',
            'content',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter blog title'
            }),

            'image' : forms.FileInput(),

            'content': forms.Textarea(attrs={
                'id' : 'id_content'
            })
        }

    def clean_content(self):

        content = self.cleaned_data.get('content')

        plain_text = strip_tags(content).strip()

        if not plain_text:
            raise forms.ValidationError(
                "Content is required."
            )

        return content


# =================== EditProfile Form ========================
class EditProfileForm(forms.ModelForm):

    class Meta:
        model = BlogUser

        fields = [
            'email',
            'first_name',
            'last_name'
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # self.fields['username'].disabled = True


    def clean_email(self):

        email = self.cleaned_data['email']

        if BlogUser.objects.exclude(
            pk=self.instance.pk
        ).filter(
            email=email
        ).exists():

            raise forms.ValidationError(
                "Email already exists."
            )

        return email

    def clean_content(self):
    
        content = self.cleaned_data.get('content')
    
        plain_text = strip_tags(content).strip()
    
        if not plain_text:
            raise forms.ValidationError(
                "Content is required."
            )
    
        return content


# =================== Contact Form ========================
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter your email'
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'placeholder': 'Enter subject'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Write your message here...',
                    'rows': 8
                }
            )
        }

    def clean_message(self):

        message = self.cleaned_data['message']
        words = len(message.split())

        if words > 200:
            raise forms.ValidationError(
                "Maximum 200 words allowed."
            )

        return message


# =================== Feedback Form ========================
class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = [
            'feedback'
        ]

        widgets = {
            'feedback': forms.Textarea(
                attrs={
                    'placeholder': 'Share your suggestion or feedback...',
                    'rows': 8
                }
            )
        }

    def clean_feedback(self):

        feedback = self.cleaned_data['feedback']
        words = len(feedback.split())

        if words > 200:
            raise forms.ValidationError(
                "Maximum 200 words allowed."
            )

        return feedback