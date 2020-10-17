from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User
from django import forms


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('user_phone',)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('user_phone',)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'user_email', 
            'user_name', 
            'user_phone',
            'password1', 
            'password2', 
            ]