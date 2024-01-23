from django.urls import path
from TV_Series_Library import views

urlpatterns = [
    path('<str:series_name>/<int:season_number>/', views.season, name='all_episodes_in_season'),
    path('<str:series_name>/<int:season_number>/<int:episode_number>/', views.episode_info, name='episode_info'),
    path('<str:series_name>-<int:release_year>/details/', views.details, name='details'),
    path('add/', views.add_series, name='add_series'),
    path('update/', views.update_series_info, name='update_series_info'),
    path('delete/', views.delete_series, name='delete_series'),
    path('', views.index, name='series'),
    path('<str:series_name>/', views.series, name='all_seasons'),
]