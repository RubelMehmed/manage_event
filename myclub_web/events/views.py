from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event
from .forms import VenueForm
# Create your views here.


# def home(request):
#     return render(request, 'home.html', {})

def add_venue(request):
    return render(request, 'events/add_venue.html', {})


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {
        'event_list': event_list
    })


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Mehmed"
    month = month.capitalize()

    # convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # create calender object
    cal = HTMLCalendar().formatmonth(year, month_number)

    # get current year
    now = datetime.now()
    current_year = now.year

    # get current time
    time = now.strftime('%I:%M %p')

    return render(request, 'home.html', {
        "name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time,
    })
