from rest_framework import serializers
from .models import Event, ProductListingsInEvent, EventListingsInCity, Ticket
from cities.serializers import CitiesPageSerializer
from books.serializers import BookSerializer, ProductSerializer
from cities.serializers import CitiesPageSerializer
from users.serializers import UserSerializer


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["city"] = CitiesPageSerializer(instance=instance.city).data
        rep["book"] = BookSerializer(instance=instance.book).data
        return rep


class ProductListingsInEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductListingsInEvent
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["event"] = EventSerializer(instance=instance.event).data
        rep["product"] = ProductSerializer(instance=instance.product).data
        return rep


class EventListingsInCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventListingsInCity
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["event"] = EventSerializer(instance=instance.event).data
        rep["city"] = CitiesPageSerializer(instance=instance.city).data
        return rep


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["event"] = EventSerializer(instance=instance.event).data
        rep["user"] = UserSerializer(instance=instance.user).data
        return rep
