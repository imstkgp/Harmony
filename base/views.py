from django.shortcuts import render
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework import viewsets, mixins
from base.models import Language
from rest_framework.response import Response
from base.serializers import LanguageSerializer

class CreateListRetrieveUpdateViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, `update` and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

class LanguageViewSet(NestedViewSetMixin, CreateListRetrieveUpdateViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
    model = Language

    def list(self, request):
        queryset = Language.objects.all()
        serializer = LanguageSerializer(queryset, many=True)
        response = {'success': True, 'language':serializer.data}
        return Response(response)

    def get_queryset(self):
        qs = Language.objects.all()
        return qs