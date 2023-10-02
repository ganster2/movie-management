# Generated by Django 4.2.5 on 2023-09-21 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0050_movie_davomiylogi_movie_homiy_movie_janr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='views',
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
