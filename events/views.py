from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm
from datetime import date

@login_required
def home(request):
    today = date.today()
    
    # Все события — для календаря
    events = Event.objects.all().order_by('date', 'time')

    # Только за сегодня и будущее — для текстового списка
    visible_events = Event.objects.filter(date__gte=today).order_by('date', 'time')

    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.user = request.user
            new_event.save()
            return redirect('home')

    return render(request, 'events/home.html', {
        'events': events,
        'visible_events': visible_events,
        'form': form
    })

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm(instance=event)

    return render(request, 'events/edit_event.html', {
        'form': form,
        'event': event
    })

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('home')

def wait_screen(request):
    today = date.today()
    queue = Event.objects.filter(date=today).order_by('time')
    return render(request, 'events/waiting.html', {'queue': queue})
