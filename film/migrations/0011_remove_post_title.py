# Generated by Django 2.0.8 on 2018-09-03 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0010_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
