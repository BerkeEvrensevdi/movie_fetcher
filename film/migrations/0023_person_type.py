# Generated by Django 2.0.8 on 2018-09-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0022_auto_20180907_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='type',
            field=models.CharField(default='', max_length=20),
        ),
    ]
