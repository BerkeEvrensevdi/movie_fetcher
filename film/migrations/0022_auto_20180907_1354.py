# Generated by Django 2.0.8 on 2018-09-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0021_auto_20180907_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='Biography',
            new_name='biography',
        ),
        migrations.AddField(
            model_name='movie',
            name='video_url',
            field=models.URLField(blank=True, max_length=250),
        ),
    ]