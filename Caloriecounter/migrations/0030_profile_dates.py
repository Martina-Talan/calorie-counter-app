# Generated by Django 4.1.5 on 2023-11-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Caloriecounter', '0029_rename_meals_meal'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dates',
            field=models.DateField(default=True),
        ),
    ]
