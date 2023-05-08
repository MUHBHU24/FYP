# Generated by Django 4.2.1 on 2023-05-08 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to='../images/items/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='../images/avatar/'),
        ),
    ]
