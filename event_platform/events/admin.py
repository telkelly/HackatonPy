from django.contrib import admin

from .models import Location
from .models import Users
from .models import Event

admin.site.register(Location)
admin.site.register(Users)
admin.site.register(Event)