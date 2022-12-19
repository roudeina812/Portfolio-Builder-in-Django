from rest_framework import serializers
from .models import Person, Experience, InfoPers, Justification


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("__all__")


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ("__all__")


class InfoPersSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoPers
        fields = ("__all__")


class JustificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Justification
        fields = ("__all__")

