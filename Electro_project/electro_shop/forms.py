from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm


class UserSignup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
