# Generated by Django 4.2.4 on 2023-08-24 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_meal_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='photo_url',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]