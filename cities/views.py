from rest_framework import viewsets
from .models import CitiesPage
from .serializers import CitiesPageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class CitiesPageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CitiesPage.objects.all()
    serializer_class = CitiesPageSerializer


class CityDetail(RetrieveUpdateDestroyAPIView):
    queryset = CitiesPage.objects.all()
    serializer_class = CitiesPageSerializer
