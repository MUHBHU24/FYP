from .models import User
from django.contrib.auth.forms import UserCreationForm


class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'city', 'username', 'password1', 'password2')