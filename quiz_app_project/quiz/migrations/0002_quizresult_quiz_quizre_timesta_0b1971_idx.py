# Generated by Django 5.1.4 on 2024-12-09 00:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name='quizresult',
            index=models.Index(fields=['timestamp'], name='quiz_quizre_timesta_0b1971_idx'),
        ),
    ]
