from django.db import models

class Location(models.Model):
    name = models.CharField('Location Name', max_length=255)
    address = models.CharField(max_length=255)
    zip_code = models.CharField('Zip Code', max_length=255)
    phone = models.CharField('Contact Phone', max_length=155)
    web = models.URLField('Web Address')
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.name

class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=255)
    date = models.DateTimeField('Event Date')
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    host = models.CharField(max_length=155)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(Users)

    def __str__(self):
        return self.name
