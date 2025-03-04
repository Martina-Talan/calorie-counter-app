# Generated by Django 4.1.5 on 2023-11-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Caloriecounter', '0041_alter_profile_steps'),
    ]

    operations = [
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_steps', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='steps',
        ),
    ]
