# Generated by Django 2.0.8 on 2020-06-12 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_recommended_movies'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='spec_id',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]
