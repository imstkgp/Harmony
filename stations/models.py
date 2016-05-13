from __future__ import unicode_literals

from django.db import models
from base.models import Language

class Station(models.Model):
    name = models.CharField(max_length=300)
    country_code = models.CharField(max_length=50, null=True, blank=True)
    country_name = models.CharField(max_length=300, null=True, blank=True)
    region = models.CharField(max_length=300, null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    thumb_url = models.URLField(max_length=500, null=True, blank=True)
    stream_url = models.URLField(max_length=500, null=True, blank=True)
    website = models.CharField(max_length=500, null=True, blank=True)
    stationId = models.IntegerField(default=0)
    genre_id = models.IntegerField(default=0)
    genre_name = models.CharField(max_length=300, null=True, blank=True)
    genre_description = models.CharField(max_length=1000, null=True, blank=True)
    language = models.ForeignKey(Language, related_name='language', null=True, blank=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name

class Favourite(models.Model):
    station = models.OneToOneField(Station, related_name='fav_station')
    count = models.IntegerField(default=0)

class MostPlayed(models.Model):
    station = models.OneToOneField(Station, related_name='most_played_station')
    count = models.IntegerField(default=0)
