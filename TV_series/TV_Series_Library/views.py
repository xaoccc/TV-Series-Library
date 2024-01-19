from django.db.models import Q
from django.shortcuts import render
from faker import Faker

from TV_Series_Library.models import Season, Episode, Series

def index(request):
    all_series = Series.objects.all().order_by("release_year")
    context = {
        'all_series': all_series
    }
    return render(request, 'index.html', context)


def series(request, series_name):
    query_object = Season.objects.filter(series__name=series_name).order_by("id")

    context = {
        'all_seasons': query_object,
        'series_name': series_name
    }

    return render(request, 'series.html', context)


def details(request, series_name):
    series = Series.objects.get(name=series_name)

    context = {
        'series': series,

    }

    return render(request, 'details.html', context)

def season(request, series_name, season_number):
    query_object = Episode.objects.filter(Q(season__series__name=series_name) & Q(season__id=season_number))

    context = {
        'all_episodes': query_object,
        'series_name': series_name,
        'season_number': season_number
    }

    return render(request, 'seasons.html', context)

def episode_info(request, series_name, season_number, episode_number):
    query_object = Episode.objects.filter(Q(series__name=series_name) & Q(season__id=season_number)).get(number=episode_number)


    context = {
        'episode_name': query_object.name,
        'episode_number': query_object.number,
        'plot': Faker().paragraph(nb_sentences=10)
    }

    return render(request, 'episodes.html', context)
