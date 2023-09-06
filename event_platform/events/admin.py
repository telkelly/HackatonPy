from django.contrib import admin

from .models import Location
from .models import Users
from .models import Event

# admin.site.register(Location)
admin.site.register(Users)
# admin.site.register(Event)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'location'), 'date', 'description', 'host')
    list_display = ('name', 'date', 'location')
    list_filter = ('date', 'location')
    ordering = ('-date',)
