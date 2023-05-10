# Generated by Django 4.2.1 on 2023-05-10 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0002_alter_message_messagepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='upvoteCount',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeUpvoted', models.DateTimeField(auto_now_add=True)),
                ('upvoter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvote_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='upvote',
            field=models.ManyToManyField(blank=True, related_name='upvoteCount', to='social.upvote'),
        ),
    ]