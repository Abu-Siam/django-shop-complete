from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import fields


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,max_length=254, help_text='Required. Inform a valid email address.', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        labels = {
            'username': 'Username',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LoginForm(AuthenticationForm):
    email = forms.EmailField(required=True,max_length=254, help_text='Required. Inform a valid email address.', widget=forms.EmailInput(attrs={'class': 'form-control','autofocus':True}),label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))