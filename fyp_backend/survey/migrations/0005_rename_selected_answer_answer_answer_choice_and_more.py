# Generated by Django 4.2.1 on 2023-05-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_alter_survey_item_image_alter_user_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='selected_answer',
            new_name='answer_choice',
        ),
        migrations.AlterField(
            model_name='survey',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]