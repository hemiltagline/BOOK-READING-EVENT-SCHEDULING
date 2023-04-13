from .models import Genre, Book, Product
from .serializers import GenreSerializer, BookSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from backend.utils import OrganizerPermission
from rest_framework import viewsets


class GenreDetail(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(created_by=request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        OrganizerPermission(request)
        data = request.data
        data["created_by"] = request.user.id
        data["updated_by"] = request.user.id
        serializer = self.get_serializer(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def patch(self, request, pk=None):
        OrganizerPermission(request)
        data = request.data
        data["updated_by"] = request.user.id
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        OrganizerPermission(request)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"id": pk, "message": "Genre deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class BookDetail(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(created_by=request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        OrganizerPermission(request)
        data = request.data
        data["created_by"] = request.user.id
        data["updated_by"] = request.user.id
        serializer = self.get_serializer(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def patch(self, request, pk=None):
        OrganizerPermission(request)
        data = request.data
        data["updated_by"] = request.user.id
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        OrganizerPermission(request)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"id": pk, "message": "Book deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class ProductDetail(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(created_by=request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        OrganizerPermission(request)
        data = request.data.copy()
        data["created_by"] = request.user.id
        data["updated_by"] = request.user.id
        serializer = self.get_serializer(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def patch(self, request, pk=None):
        OrganizerPermission(request)
        data = request.data
        data["updated_by"] = request.user.id
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        OrganizerPermission(request)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"id": pk, "message": "Product deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
