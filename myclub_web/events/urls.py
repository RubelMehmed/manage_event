from django.urls import path
from . import views

urlpatterns = [
    # Path Converts
    #int: numbers
    #str: strings
    # path: paths or whole urls
    # slug: hyphen-and-underscore
    # UUID: universally unique identifier
    path('', views.home, name="home"),
    path('<int:year>/<str:month>', views.home, name="home"),
    path('events', views.all_events, name="list-events"),
    path('add_venue', views.add_venue, name='add-venue')

]

# source virt/Scripts/activate
