from rest_framework import viewsets, mixins
from rest_framework.response import Response
from models import Station, Favourite, MostPlayed
from serializers import FavouriteSerializer, MostPlayedSerializer, StationHayStackSerializer, StationSerializer
from rest_framework.decorators import api_view
from drf_haystack.viewsets import HaystackViewSet
from drf_haystack.filters import HaystackFilter
from django.db.models import Count
from base.authentication import get_token_status
from rest_framework import exceptions
from users.models import User, Device
from itertools import chain
from django.db.models import F
from rest_framework.mixins import CreateModelMixin
from haystack.query import SearchQuerySet
from base import utils
from django.http import HttpResponse
import json
from django.db.models import Q

#Haystack filter think pagination params are actual query params, so get rid of them
class PaginatedHayStackFilter(HaystackFilter):
    def build_filter(self,view,filters=None):
        if filters:
            filters = filters.copy() #To avoid any references
            for i in ['limit','offset','format','sort']:
                filters.pop(i,None)
            for field in filters.keys():
                if field.endswith('__range') or field.endswith('__in'):
                    filters.pop(field)
        terms,exclude_terms = super(PaginatedHayStackFilter,self).build_filter(view,filters)
        return terms,exclude_terms

class StationDataViewSet(HaystackViewSet, CreateModelMixin):
    queryset = Station.objects.exclude(active=False).all()
    index_models = [Station]
    filter_backends = [PaginatedHayStackFilter]
    document_uid_field = 'unique_id'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StationSerializer
        else:
            return StationHayStackSerializer

    def list(self, request):
        state, user = get_token_status(request)
        if user:
            station_qs = super(StationDataViewSet,self).get_queryset()
            station_qs = station_qs.exclude(active=False)
            range_filters = {i:j.split(',') for i,j in self.request.GET.items() if (i.split('__')[-1] in ['in','range']) and j}
            if range_filters:
                station_qs = station_qs.filter(**range_filters)

            sort_from_query = self.request.GET.get("sort",None)
            if sort_from_query:
                sort_params = sort_from_query.split(',')
                station_qs = station_qs.order_by(*sort_params)

            fav_qs = Favourite.objects.filter(station__active=True).order_by('-count')[:10]
            most_played_qs = MostPlayed.objects.filter(station__active=True).order_by('-count')[:10]
            station_serliazer = StationHayStackSerializer(station_qs, many=True)
            favourite_serliazer = FavouriteSerializer(fav_qs, many=True)
            most_played_serliazer = MostPlayedSerializer(most_played_qs, many=True)

            response = {'success': True, 'station':station_serliazer.data, 'favourite':favourite_serliazer.data, 'most_played':most_played_serliazer.data}
            return Response(response)


@api_view(['GET', 'POST'])
def FavouriteViewSet(request, format=None):
    state, user = get_token_status(request)
    if user:
        if request.method == 'GET':
            snippets = Favourite.objects.filter(station__active=True).order_by('-count')[:10]
            serializer = FavouriteSerializer(snippets, many=True)
            response = {'success': True, 'favourite':serializer.data}
            return Response(response)

        elif request.method == 'POST':
            station = Station.objects.filter(stationId=request.data.get('station_id', 0)).last()
            response = {}
            if station:
                instance, created = Favourite.objects.get_or_create(station = station)
                instance.count = F('count') + 1
                instance.save()
                response['success'] = True
                response['message'] = 'Favourite updated successfully'
            else:
                response['success'] = False
                response['message'] = 'Failed to updated Favourite'

            return Response(response)

@api_view(['GET', 'POST'])
def MostPlayedViewSet(request, format=None):
    state, user = get_token_status(request)
    if user:
        if request.method == 'GET':
            snippets = MostPlayed.objects.filter(station__active=True).order_by('-count')[:10]
            serializer = MostPlayedSerializer(snippets, many=True)
            response = {'success': True, 'most_played':serializer.data}
            return Response(response)

        elif request.method == 'POST':
            station = Station.objects.filter(stationId=request.data.get('station_id', 0)).last()
            response = {}
            if station:
                instance, created = MostPlayed.objects.get_or_create(station = station)
                instance.count = F('count') + 1
                instance.save()
                response['success'] = True
                response['message'] = 'Most played updated successfully'
            else:
                response['success'] = False
                response['message'] = 'Failed to updated Most played'

        return Response(response)


@api_view(['POST'])
def Genre(request, format=None):
    state, user = get_token_status(request)
    if request.method == 'POST':
        try:
            data = request.data
            device_model = data.get('device_model', '')
            os = data.get('os', '')
            os_version = data.get('os_version', '')
            device_id = data.get('device_id', '')
            app_version = data.get('app_version', '1.0')
            notification_token = data.get('notification_token', '')
            lat = data.get('lat', 0)
            long = data.get('long', 0)
            if not user:
                user =User(
                    device_id = device_id,
                    latitude=lat,
                    longitude=long
                )
                user.save()

            device = Device(
                    user=user,
                    device_model=device_model,
                    os=os,
                    os_version=os_version,
                    device_id=device_id,
                    app_version=app_version,
                    notification_token=notification_token
            )
            device.save()

            required_genre = ["Bollywood", "Hindi"]
            snippets = Station.objects.filter(active=True).values('genre_id', 'genre_name', 'genre_description').annotate(count=Count('genre_name'))
            temp_snippets = snippets.filter(genre_name__in=required_genre)
            snippets = snippets.extra(order_by=('-count',))[:13]
            snippets = list(chain(temp_snippets, snippets))
            return Response({"genre":snippets, "token":user.secret_key, "success":True})

        except Exception as e:
            print e
            return Response({"success":False, "message":"Server error"})


@api_view(['GET', 'POST'])
def ModifyStationViewSet(request, format=None):
    state, user = get_token_status(request)
    if user:
        if request.method == 'GET':
            snippets = Station.objects.all().values('stationId', 'stream_url')
            snippets = list(snippets)
            response = {'success': True, 'count':len(snippets), 'station':snippets}
            return Response(response)

        elif request.method == 'POST':
            inactive_ids_list = request.data.get('station_id', [])
            Station.objects.filter(stationId__in=inactive_ids_list).update(active=False)
            Station.objects.filter(~Q(stationId__in=inactive_ids_list)).update(active=True)
            response = {'success': True, 'station':'Stations updated successfully'}

        return Response(response)

def autocomplete(request):
    default_parameters = ["q", "offset"]
    offset = int(request.GET.get('offset', 0))
    limit = 10
    query = request.GET.get('q', '')
    extra_filters = {i:j for i,j in request.GET.items() if i not in default_parameters}
    stations_sqs = SearchQuerySet().models(Station).filter(**extra_filters).autocomplete(name=query)[offset:limit]
    utils.execute_highlighter(query, "name", stations_sqs)
    stations = [{
                      "stationId": result.stationId,
                      "name": result.name,
                      "thumb_url": result.thumb_url,
                      "image_url": result.image_url,
                      "stream_url": result.stream_url,
                      "genre_id" : result.genre_id,
                      "genre_name" : result.genre_name
                  } for result in stations_sqs]
    the_data = json.dumps({
        "q": query,
        "station": stations
    })
    return HttpResponse(the_data, content_type='application/json')