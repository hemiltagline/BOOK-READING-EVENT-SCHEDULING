from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from .serializers import (
    UserSerializer,
    UserTokenObtainPairSerializer,
    UserUpdateSerializer,
)
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


def get_updated_user_type(db_user_type, new_user_type):
    if new_user_type in db_user_type:
        return db_user_type
    else:
        db_user_type.append(new_user_type)
        user_type = ",".join(db_user_type)
        return [user_type]


class UserCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        if email:
            user_type = request.data.get("user_type", None)
            if not user_type:
                return Response(
                    {"detail": "Please provide user type."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user = User.objects.filter(email__iexact=email).first()
            if user:
                user.user_type = get_updated_user_type(user.user_type, user_type)
                user.save()
            else:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save()

            serialized_user = self.get_serializer(user).data
            return Response(serialized_user, status=status.HTTP_201_CREATED)


class UserDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# User = get_user_model()


class UserUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    allowed_methods = ["PATCH"]

    def get_object(self):
        return self.request.user


class UserLoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = UserTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        if "user_type" not in request.data:
            return Response(
                {"error": "user_type is required."}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response_data = serializer.validated_data.copy()

        return Response(response_data)
