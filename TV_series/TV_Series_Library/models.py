from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Series(models.Model):
    GENRES = (
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('Action', 'Action'),
        ('Thriller', 'Thriller'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror'),
        ('Adventure', 'Adventure'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Biography', 'Biography'),
        ('Crime', 'Crime'),
        ('Mystery', 'Mystery'),
        ('Animation', 'Animation'),
        ('Family', 'Family'),
        ('Romance', 'Romance'),
        ('History', 'History'),
        ('War', 'War'),
        ('Western', 'Western'),
        ('Musical', 'Musical'),
        ('Drama', 'Drama'),
    )

    name = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2024)])
    genres = ArrayField(models.CharField(max_length=10, choices=GENRES), size=4)
    director = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('name', 'release_year')

    def __str__(self):
        return self.name


class Season(models.Model):
    series = models.ManyToManyField(Series, related_name="series_seasons")

    def __str__(self):
        return f"Season {self.pk}"


class Episode(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField(validators=[MaxValueValidator(50)])
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.series.name} S{self.season.pk} E{self.number}"

    class Meta:
        unique_together = ('number', 'season', 'series')
