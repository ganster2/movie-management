# Generated by Django 4.2.5 on 2023-09-21 13:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0052_review_likes_delete_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='likes',
        ),
        migrations.AddField(
            model_name='movie',
            name='likes',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
