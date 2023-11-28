from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from .models import Event
from django.http import HttpResponseRedirect
from .forms import EventForm, LocationForm


def home(request):
    return render(request, "base/home.html", {})


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/events.html', {'event_list': event_list})


def event_detail(request, event_id):
    event = get_object_or_404(Event, pk = event_id)
    return render(request, 'events/event_detail.html', {'event': event})


def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-events')
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
            return redirect('add-event')
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


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance = event)
    if form.is_valid():
        form.save()
        return redirect('list-events')

    return render(request, 'events/update_event.html', {'form': form, 'event': event})


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user == event.host:
        event.delete()
        messages.success(request, ("Event deleted"))
        return redirect('list-events')
    else:
        messages.success(request, ("Event cann't be deleted. Login as the host"))
        return redirect('login')


@login_required
def add_attends(request, event_id):

    event = Event.objects.get(pk=event_id)

    if request.user in event.attendees.all():
        pass
    else:
        event.attendees.add(request.user)
        event.save()

    return redirect('event', event_id = event.id)


@login_required
def user_events(request):
    current_user = request.user

    user_host = Event.objects.filter(host=current_user)

    return render(request, 'events/user_events.html', {'user_events': user_host})


@login_required
def user_attending_events(request):
    current_user = request.user

    attending_events = Event.objects.filter(attendees=current_user)

    return render(request, 'events/attending_events.html', {'attending_events': attending_events})