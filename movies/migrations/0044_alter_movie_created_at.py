# Generated by Django 4.2.5 on 2023-09-20 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0043_alter_movie_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]