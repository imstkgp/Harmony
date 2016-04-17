from rest_framework import serializers
from base.models import Language

class LanguageSerializer(serializers.ModelSerializer):
   class Meta:
        model = Language
        resource_name = 'language'