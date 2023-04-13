from rest_framework import viewsets
from .models import CitiesPage
from .serializers import CitiesPageSerializer
from rest_framework.permissions import IsAuthenticated
from backend.utils import OrganizerPermission
from rest_framework import status
from rest_framework.response import Response


class CitiesPageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CitiesPage.objects.all()
    serializer_class = CitiesPageSerializer

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
        instance = self.get_object()
        data["updated_by"] = request.user.id
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        OrganizerPermission(request)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"id": pk, "message": "City deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
