from rest_framework import serializers
from .models import User, Survey, Question, Answer, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'city')

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'title', 'created_by', 'created_at', 'getImage', 'urlSlug', )

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('survey', 'question_text')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('question', 'answer_choice')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('survey', 'user', 'comment_text', 'created_at')
