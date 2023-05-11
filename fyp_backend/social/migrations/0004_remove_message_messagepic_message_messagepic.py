# Generated by Django 4.2.1 on 2023-05-10 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_message_upvotecount_upvote_message_upvote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='messagePic',
        ),
        migrations.AddField(
            model_name='message',
            name='messagePic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messagePic', to='social.picture'),
        ),
    ]
