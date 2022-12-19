from rest_framework import viewsets
from . import models
from . import serializers


class PersonViewSet (viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    http_method_name = ['get', 'post', 'put', 'delete', 'patch']


class ExperienceViewSet (viewsets.ModelViewSet):
    queryset = models.Experience.objects.all()
    serializer_class = serializers.ExperienceSerializer
    http_method_name = ['get', 'post', 'put', 'delete', 'patch']


class JustificationViewSet (viewsets.ModelViewSet):
    queryset = models.Justification.objects.all()
    serializer_class = serializers.JustificationSerializer
    http_method_name = ['get', 'post', 'put', 'delete', 'patch']


class InfoPersViewSet (viewsets.ModelViewSet):
    queryset = models.InfoPers.objects.all()
    serializer_class = serializers.InfoPersSerializer
    http_method_name = ['get', 'post', 'put', 'delete', 'patch']
