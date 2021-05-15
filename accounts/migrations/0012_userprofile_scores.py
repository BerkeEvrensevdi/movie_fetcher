# Generated by Django 2.0.8 on 2020-06-15 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0047_auto_20200615_0610'),
        ('accounts', '0011_remove_userprofile_scores'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='scores',
            field=models.ManyToManyField(blank=True, related_name='ratings', to='film.Score'),
        ),
    ]
