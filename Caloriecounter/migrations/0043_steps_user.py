# Generated by Django 4.1.5 on 2023-11-17 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Caloriecounter', '0042_steps_remove_profile_steps'),
    ]

    operations = [
        migrations.AddField(
            model_name='steps',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
