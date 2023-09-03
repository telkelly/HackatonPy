from django.db import models

class Location(models.Model):
    name = models.CharField('Location Name', max_length=255)
    address = models.CharField(max_length=255)
    zip_code = models.CharField('Zip Code', max_length=255)
    phone = models.CharField('Contact Phone', max_length=155)
    web = models.URLField('Web Address')
    email_address = models.EmailField('Email Address')

# Create your models here.
class Event(models.Model):
    name = models.CharField('Event Name', max_length=255)
    date = models.DateTimeField('Event Date')
    location = models.CharField(max_length=155)
    host = models.CharField(max_length=155)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


