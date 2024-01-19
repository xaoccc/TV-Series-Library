from django.contrib import admin

from TV_Series_Library.models import Series, Season, Episode


# Register your models here.
@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    fields = ["name", "release_year", "genres", "director", "rating", "description"]


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    fields = ["series"]


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    fields = ["name", "number", "series", "season"]
