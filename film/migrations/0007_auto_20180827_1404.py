# Generated by Django 2.0.8 on 2018-08-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0006_auto_20180827_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='movie',
            name='topic',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
