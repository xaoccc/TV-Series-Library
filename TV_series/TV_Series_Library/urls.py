from django.urls import path
from TV_Series_Library import views

urlpatterns = [
    path('', views.index, name='series'),
    path('<str:series_name>/', views.series, name='all_seasons'),
    path('<str:series_name>/<int:season_number>/', views.season, name='all_episodes_in_season'),
    path('<str:series_name>/<int:season_number>/<int:episode_number>/', views.episode_info, name='episode_info'),
    path('<str:series_name>/details/', views.details, name='details'),
]