# Generated by Django 2.0.8 on 2018-09-05 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0013_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]