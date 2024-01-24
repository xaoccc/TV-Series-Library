from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from TV_Series_Library.models import Season, Episode, Series
from TV_Series_Library.forms import SeriesForm

def index(request):
    all_series = Series.objects.all().order_by("release_year")


    if request.method == 'GET':
        add_series_form = SeriesForm()
        update_series_form = SeriesForm(initial={'name': "NAME", 'release_year': 2020, 'genres': 'Genres',
                                                 'director': 'Director', 'rating': 0, 'description': 'Description'})
    else:
        add_series_form = SeriesForm(request.POST)
        update_series_form = SeriesForm(request.POST)

    context = {
        'all_series': all_series,
        'add_series_form': add_series_form,
        'update_series_form': update_series_form,
    }
    return render(request, 'index.html', context)


def series(request, series_name):
    query_object = Season.objects.filter(series__name=series_name).order_by("id")

    context = {
        'all_seasons': query_object,
        'series_name': series_name
    }

    return render(request, 'series.html', context)


def details(request, series_name, release_year):
    series = Series.objects.get(release_year=release_year, name=series_name)
    genres = ", ".join(series.genres)

    if request.method == "GET":
        update_series_form = SeriesForm(instance=series)

    else:
        update_series_form = SeriesForm(request.POST, instance=series)

    context = {
        'series': series,
        'genres': genres,
        'update_series_form': update_series_form
    }

    return render(request, 'details.html', context)

def season(request, series_name, season_number):
    query_object = Episode.objects.filter(Q(series__name=series_name) & Q(season__id=season_number))

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
    }

    return render(request, 'episodes.html', context)

def delete_series(request):

    if request.method == 'POST':
        try:
            series_id = request.POST.get('series_id')
            series_to_delete = Series.objects.get(id=series_id)
            series_to_delete.delete()
        except Series.DoesNotExist:
            return HttpResponse('Series not found', status=404)
    else:
        return HttpResponse('Method not allowed', status=405)
    return redirect('series')


def add_series(request):
    all_series = Series.objects.all().order_by("release_year")

    if request.method == "GET":
        add_series_form = SeriesForm()

    else:
        add_series_form = SeriesForm(request.POST)
        if add_series_form.is_valid():
            name = add_series_form.cleaned_data['name']
            release_year = add_series_form.cleaned_data["release_year"]
            genres = add_series_form.cleaned_data["genres"]
            director = add_series_form.cleaned_data["director"]
            rating = add_series_form.cleaned_data["rating"]
            description = add_series_form.cleaned_data["description"]

            Series.objects.create(name=name, release_year=release_year, genres=genres, director=director, rating=rating,
                                  description=description)

            return redirect('series')


    context = {
        'all_series': all_series,
        'add_series_form': add_series_form
    }

    return render(request, 'index.html', context)


def update_series_info(request, series_id):
    series_to_update = Series.objects.get(id=series_id)
    if request.method == "GET":
        update_series_form = SeriesForm(instance=series_to_update)

    else:
        try:
            update_series_form = SeriesForm(request.POST, instance=series_to_update)

            if update_series_form.is_valid():
                name = update_series_form.cleaned_data["name"]
                release_year = update_series_form.cleaned_data["release_year"]
                genres = update_series_form.cleaned_data["genres"]
                director = update_series_form.cleaned_data["director"]
                rating = update_series_form.cleaned_data["rating"]
                description = update_series_form.cleaned_data["description"]

                series_to_update = Series(series_to_update.id, name, release_year, genres, director, rating,
                                          description)
                series_to_update.save()

                return redirect('series')

        except Series.DoesNotExist:
            return HttpResponse('Series not found', status=404)

    context = {
        'series_to_update': series_to_update,
        'update_series_form': update_series_form,
        'series_id': series_id
    }

    return render(request, 'details.html', context)






