from .models import User, userResponse
from django.contrib.auth.forms import UserCreationForm
from django import forms


class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'city', 'username', 'password1', 'password2')


class userResponseForm(forms.ModelForm):
    class Meta:
        model = userResponse
        fields = ['selected_answer']