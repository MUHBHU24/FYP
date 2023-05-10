from .models import Message
from django.forms import ModelForm


# This is the form for creating a new message, used in the create_message view. 
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('main',)