# Generated by Django 4.1.5 on 2023-08-06 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Caloriecounter', '0002_alter_profile_activity_alter_profile_goal_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='goal_choice',
            new_name='your_goal',
        ),
    ]
