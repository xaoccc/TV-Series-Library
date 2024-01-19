# Generated by Django 4.2.4 on 2024-01-19 09:40

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2024)])),
                ('genres', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Drama', 'Drama'), ('Comedy', 'Comedy'), ('Action', 'Action'), ('Thriller', 'Thriller'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Adventure', 'Adventure'), ('Sci-Fi', 'Sci-Fi'), ('Biography', 'Biography')], max_length=10), size=4)),
                ('director', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('description', models.TextField()),
            ],
            options={
                'unique_together': {('name', 'release_year')},
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.ManyToManyField(related_name='series_seasons', to='TV_Series_Library.series')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(50)])),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TV_Series_Library.season')),
                ('series', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='TV_Series_Library.series')),
            ],
        ),
    ]
