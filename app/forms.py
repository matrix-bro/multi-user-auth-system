from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_no', 'password1', 'password2']
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'John',
        'class': INPUT_CLASSES,
        'autofocus': True
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Doe',
        'class': INPUT_CLASSES
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'john',
        'class': INPUT_CLASSES
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'john@doe.com',
        'class': INPUT_CLASSES
    }))

    phone_no = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '987654321',
        'class': INPUT_CLASSES
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': INPUT_CLASSES
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
        'class': INPUT_CLASSES
    }))

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))  