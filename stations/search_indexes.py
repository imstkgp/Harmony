from haystack import indexes
from models import Station

class StationIndex(indexes.ModelSearchIndex, indexes.Indexable):
    unique_id = indexes.IntegerField(model_attr='id')
    stationId = indexes.IntegerField(model_attr='stationId')
    name = indexes.NgramField(model_attr='name')
    country_name = indexes.CharField(model_attr='country_name', null=True)
    region = indexes.CharField(model_attr='region', null=True)
    thumb_url = indexes.CharField(model_attr='thumb_url', null=True)
    image_url = indexes.CharField(model_attr='image_url', null=True)
    stream_url = indexes.CharField(model_attr='stream_url', null=True)
    website = indexes.CharField(model_attr='website', null=True)
    genre_id = indexes.IntegerField(model_attr='genre_id')
    genre_name = indexes.CharField(model_attr='genre_name', null=True)
    genre_description = indexes.CharField(model_attr='genre_description', null=True)
    active = indexes.BooleanField(model_attr='active')
    language = indexes.IntegerField(model_attr='language_id', null=True)

    class Meta:
        model = Station

    def index_queryset(self,using=None):
        return self.get_model().objects.filter(active=True)

