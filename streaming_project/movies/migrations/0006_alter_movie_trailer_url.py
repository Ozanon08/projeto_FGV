# Generated by Django 4.2.3 on 2023-07-27 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_trailer_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='trailer_url',
            field=models.URLField(),
        ),
    ]
