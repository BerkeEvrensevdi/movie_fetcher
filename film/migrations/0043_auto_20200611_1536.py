# Generated by Django 2.0.8 on 2020-06-11 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0042_auto_20200611_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
