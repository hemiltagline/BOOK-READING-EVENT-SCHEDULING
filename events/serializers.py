from rest_framework import serializers
from .models import Event
from cities.serializers import CitiesPageSerializer
from books.serializers import BookSerializer


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["city"] = CitiesPageSerializer(instance=instance.city).data
        rep["book"] = BookSerializer(instance=instance.book).data
        return rep
