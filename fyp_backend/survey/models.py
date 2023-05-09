from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from autoslug import AutoSlugField


class User(AbstractUser):  # Extends the default Django User model with additional fields and methods
    city = models.CharField(max_length=60, blank=False, null=False)
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    avatar = models.ImageField(upload_to='images/avatar/', blank=True, null=True)

    def __str__(self) -> str:
        return self.username

    def to_dict(self) -> dict:  # Returns a dictionary representation of the user
        return {
            'id': self.id,
            'first_name': self.first_name,
            'username': self.username,
            'city': self.city,
            'age': self.age,
            'bio': self.bio,
            # Return the URL of the avatar if it exists, otherwise return None
            'avatar': self.avatar.url if self.avatar else None,
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


class Survey(models.Model):  # A survey contains one question and multiple answers to choose from
    title = models.CharField(
        max_length=20, unique=True, blank=False, null=False)
    item_image = models.ImageField(upload_to='', blank=True, null=True)
    # if user is deleted, delete all surveys created by user
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Used for URL routing (e.g. /survey/<slug>)
    slug = AutoSlugField(populate_from='title', unique=True)

    class Meta:
        ordering = ['-created_at']  # Order surveys by most recent

    # urlSlug is a property that returns the URL of the survey
    def urlSlug(self) -> str: 
        return f'/survey/{self.slug}'

    # Image URL for the survey item
    def getImage(self) -> str:
        if self.item_image:
            return self.item_image.url
        else:
            return ""

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_candidate = slugify(self.title)
            self.slug = self._generate_unique_slug(slug_candidate)
        super(Survey, self).save(*args, **kwargs)

    # Generate a unique slug for the survey (e.g. "my-survey" -> "my-survey-abc1") if it already exists in the database
    def _generate_unique_slug(self, slug_candidate):
        MAX_RETRIES = 10 # Maximum number of times to try generating a unique slug
        for i in range(MAX_RETRIES):
            if not Survey.objects.filter(slug=slug_candidate).exists():
                return slug_candidate

            # If slug_candidate already exists, append a random 4-character string and try again
            slug_candidate = f"{slug_candidate}-{get_random_string(4)}"

        raise ValueError("Could not generate a unique slug for the survey") # else raise an error if we've tried too many times

    def __str__(self) -> str:
        return self.title


class Question(models.Model):  # A question belongs to a survey and has multiple answer choices
    survey = models.OneToOneField(
        Survey, on_delete=models.CASCADE, primary_key=True)
    question_text = models.CharField(
        max_length=50, blank=False, null=False, unique=True, help_text="Enter the question text")

    def __str__(self) -> str:
        return self.question_text


class Answer(models.Model):  # An answer belongs to a question and is selected by a user
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_choice = models.CharField(max_length=15, blank=False, null=False)
    # Users who selected this answer (for location later)
    users_voted = models.ManyToManyField(
        User, related_name="users_voted", blank=True)
    # Number of users who selected this answer
    vote_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.answer_choice


class Comment(models.Model):  # A comment belongs to a survey and is made by a user
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(
        max_length=100, blank=False, null=False, help_text="Enter your comment")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}: {self.comment_text}"
