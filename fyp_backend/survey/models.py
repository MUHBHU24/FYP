from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser): # Extends the default Django User model with additional fields and methods 
    city = models.CharField(max_length=60, blank=False, null=False)
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    avatar = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self) -> str:
        return self.username

    def to_dict(self) -> dict: # Returns a dictionary representation of the user
        return {
            'id': self.id,
            'first_name': self.first_name,
            'username': self.username,
            'city': self.city,
            'age': self.age,
            'bio': self.bio,
            'avatar': self.avatar.url if self.avatar else None, # Return the URL of the avatar if it exists, otherwise return None   
        }
    
    def to_dict_simple(self) -> dict:
        return {
            'id': self.id,
            'username': self.username,
            'avatar': self.avatar.url if self.avatar else None,           
        }
    
    def save(self, *args, **kwargs) -> None:
        if self.avatar == None:
            self.avatar = 'images/default_avatar.png'
        super(User, self).save(*args, **kwargs)


class Survey(models.Model): # A survey contains one question and multiple answers to choose from
    title = models.CharField(max_length=20, unique=True, blank=False, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) # if user is deleted, delete all surveys created by user
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Question(models.Model): # A question belongs to a survey and has multiple answer choices
    survey = models.OneToOneField(Survey, on_delete=models.CASCADE, primary_key=True)
    question_text = models.CharField(max_length=50, blank=False, null=False, unique=True, help_text="Enter the question text")

    def __str__(self) -> str:
        return self.question_text


class Answer(models.Model): # An answer belongs to a question and is selected by a user
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=15, blank=False, null=False)
    users_voted = models.ManyToManyField(User, related_name="users_voted", blank=True) # Users who selected this answer (for location later)
    vote_count = models.IntegerField(default=0) # Number of users who selected this answer

    def __str__(self) -> str:
        return self.selected_answer


class Comment(models.Model): # A comment belongs to a survey and is made by a user
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=100, blank=False, null=False, help_text="Enter your comment")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}: {self.comment_text}"