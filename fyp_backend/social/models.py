from django.db import models
from survey.models import User

# Create your models here.


class Picture(models.Model):
    pic = models.ImageField(upload_to='messagePics')
    # links the picture to the message
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pic_author') 

    def __str__(self) -> str:
        return f'picture by {self.author}'


class Reply(models.Model):
    replier = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replier')
    timeReply = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length="50", blank=True, null=True)

    def __str__(self) -> str:
        return f'reply message by {self.replier} at {self.timeReply}'


class Upvote(models.Model):
    # links the person who upvoted to the message they upvoted
    upvoter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvote_by')
    # keeps track of the time the user upvoted the message
    timeUpvoted = models.DateTimeField(auto_now_add=True)




class Message(models.Model):
    main = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msg_author')
    timePosted = models.DateTimeField(auto_now_add=True)
    messagePic = models.ImageField(upload_to='../images/messages/', null=True, blank=True)
    # keeps track of the number of upvotes for each message
    upvoteCount = models.IntegerField(default=0)
    # keeps track of the users who upvoted the message and prevents them from upvoting more than once
    upvote = models.ManyToManyField(Upvote, blank=True, related_name='upvote')
    # keeps track of the number of replies for each message
    replyCount = models.IntegerField(default=0)
    # keeps track of the users who replied to the message
    reply = models.ManyToManyField(Reply, blank=True, related_name='reply')

    def __str__(self):
        return f"Message by {self.author.username} at {self.timePosted}"

    def update_upvote_count(self):
        self.upvoteCount = self.upvote.count()
        self.save()

    def update_reply_count(self):
        self.replyCount = self.reply.count()
        self.save()
