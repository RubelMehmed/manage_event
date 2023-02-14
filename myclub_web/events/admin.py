from django.contrib import admin
from .models import Venue
from .models import MyClubUser
from .models import Event
#from .models import Venue, MyClubUser, Event

# Register your models here.
#admin.site.register(Venue, MyClubUser, Event)

# admin.site.register(Venue)
admin.site.register(MyClubUser)
# admin.site.register(Event)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'venue')
    ordering = ('name',)
    search_fields = ('name', 'event_date', 'venue')
