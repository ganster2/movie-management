# Generated by Django 4.2.5 on 2023-09-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0023_moviepart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviepart',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
