# Generated by Django 4.2.3 on 2023-08-01 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_movie_favorite_of_users_movie_watched_by_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='trailer_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
