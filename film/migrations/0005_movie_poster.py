# Generated by Django 2.0.8 on 2018-08-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0004_auto_20180822_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, upload_to='poster_image'),
        ),
    ]