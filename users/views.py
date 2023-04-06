from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth import get_user_model


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class UserCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


User = get_user_model()


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
