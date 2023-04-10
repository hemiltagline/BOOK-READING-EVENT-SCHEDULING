from rest_framework import serializers
from .models import CitiesPage


class CitiesPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitiesPage
        fields = "__all__"
