# Generated by Django 2.0.8 on 2020-06-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0041_person_id_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
