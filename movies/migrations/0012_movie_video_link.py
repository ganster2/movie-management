# Generated by Django 4.2.4 on 2023-09-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video_link',
            field=models.URLField(default='https://example.com'),
        ),
    ]
