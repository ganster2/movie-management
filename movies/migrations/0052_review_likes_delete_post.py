# Generated by Django 4.2.5 on 2023-09-21 13:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0051_remove_movie_dislikes_remove_movie_likes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='likes',
            field=models.ManyToManyField(related_name='review_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
