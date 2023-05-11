from .models import Message, Picture, Reply
from rest_framework import serializers
from survey.serializers import UserSerializer


class PictureSerializer(serializers.ModelSerializer):
    pic = serializers.SerializerMethodField()

    class Meta:
        model = Picture
        fields = ('id', 'pic', 'author',)

    def get_pic(self, obj):
        if obj.pic:
            return self.context['request'].build_absolute_uri(obj.pic.url)
        return ''


class MessageSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    city = UserSerializer(read_only=True, many=False)
    message = serializers.ImageField(required=False, allow_null=True, max_length=None, use_url=True)

    class Meta:
        model = Message
        fields = ('id', 'main', 'author', 'timePosted', 'upvoteCount', 'upvote', 'messagePic', 'city', 'message', )


class ReplySerializer(serializers.ModelSerializer):
    replier = UserSerializer(read_only=True)

    class Meta:
        model = Reply
        fields = ('id', 'replier', 'timeReply', 'text', )


class ExpandMessageSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True, many=False)
    replies = ReplySerializer(read_only=True, many=True)
    city = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Message
        fields = ('id', 'main', 'author', 'timePosted', 'upvoteCount', 'upvote', 'messagePic', 'city', 'replies')


        

