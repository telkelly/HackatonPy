from django.db.models import Q
from django.shortcuts import render
from .models import Event
from django.http import HttpResponseRedirect
from .forms import EventForm, LocationForm


def home(request):
    return render(request, "base/home.html", {})


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/events.html', {'event_list': event_list})


def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event/?submitted=True')
    else:
        form = EventForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})


def add_location(request):
    submitted = False
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_location/?submitted=True')
    else:
        form = LocationForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_location.html', {'form': form, 'submitted': submitted})


def search_event(request):
    searched = ''
    events = []

    if request.method == "POST":
        searched = request.POST.get('searched', '') 
        events = Event.objects.filter(name__icontains = searched)
    return render(request, 'events/search_event.html', {'searched': searched, 'events': events})
