from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Event, ProductListingsInEvent, EventListingsInCity, Ticket
from .serializers import (
    EventSerializer,
    ProductListingsInEventSerializer,
    EventListingsInCitySerializer,
    TicketSerializer,
)
from rest_framework.permissions import IsAuthenticated
from backend.utils import OrganizerPermission, CustomerPermission
from datetime import timedelta
from django.utils import timezone


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

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
        data["organizer"] = request.user.id
        data["created_by"] = request.user.id
        data["updated_by"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, pk=None, *args, **kwargs):
        OrganizerPermission(request)
        event_obj = Event.objects.filter(id=pk).first()
        # If the event is cancelled and cannot be cancelled, raise a ValidationError
        if event_obj.status == Event.CANCELLED and not (
            event_obj.start_time > timezone.now() + timedelta(hours=24)
        ):
            return Response(
                {"detail": "Cannot cancel event less than 24 hours before start time."},
                status=status.HTTP_400_BAD_REQUEST,
            )
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
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductListingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProductListingsInEvent.objects.all()
    serializer_class = ProductListingsInEventSerializer

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
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventListingsInCityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = EventListingsInCity.objects.all()
    serializer_class = EventListingsInCitySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(created_by=request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        OrganizerPermission(request)
        data = request.data
        data["created_by"] = request.user.id
        data["updated_by"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        OrganizerPermission(request)
        partial = kwargs.pop("partial", False)
        data = request.data
        data["updated_by"] = request.user.id
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        OrganizerPermission(request)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(user=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        CustomerPermission(request)
        data = request.data.copy()
        data["user"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        CustomerPermission(request)
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        CustomerPermission(request)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
