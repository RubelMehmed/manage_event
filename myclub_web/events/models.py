from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Venue(models.Model):
    name = models.CharField(max_length=60, verbose_name='Venue Name')
    address = models.CharField(max_length=120, verbose_name='Address')
    zip_code = models.CharField(
        max_length=25, verbose_name='Zip Code', blank=True)
    phone = models.CharField(max_length=25, verbose_name='Phone', blank=True)
    web = models.URLField(verbose_name='Web Address', blank=True)
    email_address = models.EmailField(verbose_name='Email Address')

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(verbose_name='Email Address')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField(max_length=120, verbose_name='Event Name')
    event_date = models.DateTimeField(verbose_name='Event Date')
    # venue = models.CharField(max_length=120)
    venue = models.ForeignKey(
        Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name
