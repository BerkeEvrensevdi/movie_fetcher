# Generated by Django 2.0.8 on 2018-09-10 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0023_person_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='writer',
            field=models.ManyToManyField(blank=True, related_name='writers', to='film.Person'),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(blank=True, related_name='directors', to='film.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='starring',
            field=models.ManyToManyField(blank=True, related_name='stars', to='film.Person'),
        ),
    ]
