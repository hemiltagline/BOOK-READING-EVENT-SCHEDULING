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

    def create(self, request):
        OrganizerPermission(request)
        data = request.data
        serializer = self.get_serializer(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def patch(self, request, pk=None):
        OrganizerPermission(request)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
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
