# Generated by Django 4.2.5 on 2023-09-20 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0049_alter_movie_is_premiere'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='davomiylogi',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='movie',
            name='homiy',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='movie',
            name='janr',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='movie',
            name='kompaniya',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='movie',
            name='ovozberishaktorlari',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='movie',
            name='rejesyor',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='movie',
            name='tili',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='movie',
            name='yili',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='movie',
            name='yoshcheklovi',
            field=models.CharField(default='unknown', max_length=255),
        ),
    ]
