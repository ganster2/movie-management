# Generated by Django 4.2.5 on 2023-09-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0017_movie_iframe_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_url',
            field=models.URLField(null=True),
        ),
    ]
