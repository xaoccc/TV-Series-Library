from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from TV_Series_Library.models import Season, Episode, Series
from TV_Series_Library.forms import NewSeriesForm, UpdateSeriesForm

def index(request):
    all_series = Series.objects.all().order_by("release_year")

    if request.method == 'GET':
        add_series_form = NewSeriesForm()
        update_series_form = UpdateSeriesForm()

        if request.GET.get('series_id'):
            series_id = request.GET.get('series_id')
            series_to_update = Series.objects.get(id=series_id)
            update_series_form = UpdateSeriesForm(instance=series_to_update)

    else:
        add_series_form = NewSeriesForm(request.POST)

        if request.POST.get('series_id'):

            series_id = request.POST.get('series_id')
            series_to_update = Series.objects.get(id=series_id)
            update_series_form = UpdateSeriesForm(request.POST, instance=series_to_update)

            if update_series_form.is_valid():
                name = update_series_form.cleaned_data["name"]
                release_year = update_series_form.cleaned_data["release_year"]
                genres = update_series_form.cleaned_data["genres"]
                director = update_series_form.cleaned_data["name"]
                rating = update_series_form.cleaned_data["rating"]
                description = update_series_form.cleaned_data["description"]
                if not description:
                    description = "N/A"

                series_to_update = Series(series_to_update.id, name, release_year, genres, director, rating, description)
                series_to_update.save()
                return redirect('series')

        else:
            if add_series_form.is_valid():
                name = add_series_form.cleaned_data["name"]
                release_year = add_series_form.cleaned_data["release_year"]
                genres = add_series_form.cleaned_data["genres"]
                director = add_series_form.cleaned_data["name"]
                rating = add_series_form.cleaned_data["rating"]
                description = add_series_form.cleaned_data["description"]
                if not description:
                    description = "N/A"

                Series.objects.create(name=name, release_year=release_year, genres=genres, director=director, rating=rating, description=description)
                return redirect('series')

    context = {
        'all_series': all_series,
        'add_series_form': add_series_form,
        'update_series_form': update_series_form
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

    context = {
        'series': series,
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





