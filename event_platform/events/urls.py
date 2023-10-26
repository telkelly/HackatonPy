from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('events', views.all_events, name="list-events"),
    path('add_event', views.add_event, name='add-event'),
    path('add_location', views.add_location, name='add-location'),
    path('search_event', views.search_event, name = 'search-event'),
]
