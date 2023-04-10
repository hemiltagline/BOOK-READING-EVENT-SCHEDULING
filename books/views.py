from .models import Genre, Book
from .serializers import GenreSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status


class GenreViewSet(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def delete(self, request, pk, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response(
            {"id": pk, "message": "Genre deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class BookList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def delete(self, request, pk, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response(
            {"id": pk, "message": "Book deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
