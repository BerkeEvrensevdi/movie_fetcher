# Generated by Django 2.0.8 on 2020-06-11 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0033_remove_movie_imdb_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb',
            field=models.CharField(default='', max_length=20),
        ),
    ]
