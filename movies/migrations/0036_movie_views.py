# Generated by Django 4.2.5 on 2023-09-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0035_carousel'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
