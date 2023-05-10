from .models import Message
from rest_framework import serializers
from survey.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True, many=False)
    city = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Message
        fields = ('id', 'main', 'author', 'timePosted', 'upvoteCount', 'upvote', 'messagePic', 'city',)