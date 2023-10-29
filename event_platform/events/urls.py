from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('events', views.all_events, name="list-events"),
    path('add_event', views.add_event, name='add-event'),
    path('add_location', views.add_location, name='add-location'),
    path('search_event', views.search_event, name = 'search-event'),
    path('event/<int:event_id>', views.event_detail, name = 'event'),
    path('update_event/<int:event_id>', views.update_event, name = 'update-event'),
    path('delete_event/<int:event_id>', views.delete_event, name = 'delete-event'),
    path('add_attends/<int:event_id>', views.add_attends, name = 'add-attends'),
]
