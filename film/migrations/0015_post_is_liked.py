# Generated by Django 2.0.8 on 2018-09-06 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0014_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
    ]
