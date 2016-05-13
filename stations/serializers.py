from rest_framework import serializers
from models import Station, Favourite, MostPlayed
from rest_framework.response import Response

class FavouriteSerializer(serializers.ModelSerializer):
    station = serializers.SerializerMethodField()

    def get_station(self, obj):
        return StationHayStackSerializer(Station.objects.get(id=obj.station_id)).data

    class Meta:
        model = Favourite
        resource_name = 'favourite'

class MostPlayedSerializer(serializers.ModelSerializer):
    station = serializers.SerializerMethodField()

    def get_station(self, obj):
        return StationHayStackSerializer(Station.objects.get(id=obj.station_id)).data

    class Meta:
        model = MostPlayed
        resource_name = 'mostplayed'

class StationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = Station.objects.filter(stationId=validated_data['stationId']).last()
        if not instance:
            instance = super(StationSerializer, self).create(validated_data)
        else:
            instance = super(StationSerializer, self).update(instance, validated_data)

        return instance

    class Meta:
        model = Station

class StationHayStackSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    stationId = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    country_name = serializers.ReadOnlyField()
    region = serializers.ReadOnlyField()
    thumb_url = serializers.ReadOnlyField()
    image_url = serializers.ReadOnlyField()
    stream_url = serializers.ReadOnlyField()
    website = serializers.ReadOnlyField()
    genre_id = serializers.ReadOnlyField()
    genre_name = serializers.ReadOnlyField()
    genre_description = serializers.ReadOnlyField()
    active = serializers.ReadOnlyField()
    language = serializers.ReadOnlyField()

    def get_id(self,obj):
        try:
            return obj.id.split('.')[-1]
        except:
            return obj.id

    class Meta:
        model = Station
        resource_name = 'station'

