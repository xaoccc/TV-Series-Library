# Generated by Django 4.2.9 on 2024-01-27 14:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TV_Series_Library', '0003_alter_episode_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='genres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Drama', 'Drama'), ('Comedy', 'Comedy'), ('Action', 'Action'), ('Thriller', 'Thriller'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Adventure', 'Adventure'), ('Sci-Fi', 'Sci-Fi'), ('Biography', 'Biography'), ('Crime', 'Crime'), ('Mystery', 'Mystery'), ('Animation', 'Animation'), ('Family', 'Family'), ('Romance', 'Romance'), ('History', 'History'), ('War', 'War'), ('Western', 'Western'), ('Musical', 'Musical'), ('Drama', 'Drama')], max_length=10), size=4),
        ),
    ]