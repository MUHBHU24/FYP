from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    avatar = serializers.ImageField(source='user.avatar')

    class Meta:
        model = Comment
        fields = ['text', 'created_at', 'username', 'avatar']

