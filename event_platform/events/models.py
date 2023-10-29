from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField('Location Name', max_length=255)
    address = models.CharField(max_length=255)
    zip_code = models.CharField('Zip Code', max_length=10, blank=True)  # Changed max_length for zip_code
    phone = models.CharField('Contact Phone', max_length=20, blank=True)  # Changed max_length for phone
    web = models.URLField('Web Address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=255)
    date = models.DateTimeField('Event Date')
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    host = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(User, related_name='events_attending', blank=True)
    event_image = models.ImageField(null = True, blank = True, upload_to = "images/")

    def __str__(self):
        return self.name
