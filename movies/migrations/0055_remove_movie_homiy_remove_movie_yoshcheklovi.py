# Generated by Django 4.2.5 on 2023-09-23 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0054_remove_movie_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='homiy',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='yoshcheklovi',
        ),
    ]
