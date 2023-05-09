from .models import User, Response
from django.contrib.auth.forms import UserCreationForm
from django import forms


class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'city', 'username', 'password1', 'password2')


class responseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['selected_answer']