from .models import Message, Picture, Reply
from rest_framework import serializers
from survey.serializers import UserSerializer


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'pic', 'author',)


class ExpandMessageSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Message
        fields = ('id', 'main', 'author', 'timePosted', 'upvoteCount', 'upvote', 'messagePic', 'city',)


class ReplySerializer(serializers.ModelSerializer):
    replier = UserSerializer(read_only=True)
    reply = ExpandMessageSerializer(read_only=True, many=True)

    class Meta:
        model = Reply
        fields = ('id', 'replier', 'timeReply', 'text', )
        

class MessageSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True, many=False)
    city = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Message
        fields = ('id', 'main', 'author', 'timePosted', 'upvoteCount', 'upvote', 'messagePic', 'city',)