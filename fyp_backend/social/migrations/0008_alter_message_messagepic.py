# Generated by Django 4.2.1 on 2023-05-11 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_alter_reply_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='messagePic',
            field=models.ImageField(blank=True, null=True, upload_to='../images/messages/'),
        ),
    ]
