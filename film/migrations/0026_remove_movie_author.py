# Generated by Django 2.0.8 on 2018-09-13 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0025_movie_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='author',
        ),
    ]
