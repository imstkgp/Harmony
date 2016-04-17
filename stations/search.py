from haystack.query import SearchQuerySet
from models import Station

propertiesQuerySet = SearchQuerySet().models(Station).exclude(active=False)