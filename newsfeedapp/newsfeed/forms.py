from django import forms
from .models import News
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewsForm(forms.ModelForm):   
    class Meta:
        model = News
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')