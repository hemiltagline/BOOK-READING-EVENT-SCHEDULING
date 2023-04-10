from rest_framework import serializers
from .models import Genre, Book


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "genre", "summary", "cover_image"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["genre"] = GenreSerializer(instance=instance.genre).data
        return rep
