from django.db import models
from survey.models import User

# Create your models here.


class Picture(models.Model):
    pic = models.ImageField(upload_to='messagePics')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pic_author') 


class Message(models.Model):
    main = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msg_author')
    timePosted = models.DateTimeField(auto_now_add=True)
    messagePic = models.ManyToManyField(Picture, blank=True, related_name='messagePic')
    
    
