# Generated by Django 4.2.4 on 2023-08-23 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_meal_ingredients_alter_meal_picture_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='picture',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.meal')),
            ],
        ),
    ]
