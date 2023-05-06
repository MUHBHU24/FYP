from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser): # Extends the default Django User model with additional fields and methods 
    city = models.CharField(max_length=60, blank=False, null=False)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.username

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'first_name': self.first_name,
            'username': self.username,
            'city': self.city,
            'avatar': self.avatar.url if self.avatar else None,           
            'age': self.age,
            'bio': self.bio,
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
    description = models.CharField(max_length=50, blank=False, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model): # A question belongs to a survey and has multiple answer choices
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=50, blank=False, null=False, unique=True, help_text="Enter the question text", error_messages={'unique': "This question already exists."})
    answer_choices = models.CharField(max_length=15, blank=False, null=False)  # Store answer choices as a JSON string or delimited string

    def __str__(self) -> str:
        return self.question_text
    
    class Meta:
        # permissions = [
        #     ("add_question", "Can add question"),
        #     ("change_question", "Can change question"),
        #     ("delete_question", "Can delete question"),
        # ]
        pass


class Answer(models.Model): # An answer belongs to a question and is selected by a user
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self) -> str:
        return self.selected_answer


class Comment(models.Model): # A comment belongs to a survey and is made by a user
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=100, blank=False, null=False, help_text="Enter your comment")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}: {self.comment_text}"