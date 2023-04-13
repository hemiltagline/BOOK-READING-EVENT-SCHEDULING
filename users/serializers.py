from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import datetime
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "user_type",
            "password",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "user_type",
        ]


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user, user_type):
        token = super().get_token(user)

        # Add custom claim to the payload
        token["user_type"] = user_type

        return token

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user_type = self.initial_data.get("user_type")

        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                email=email,
                password=password,
            )

            if not user:
                raise serializers.ValidationError("Invalid email or password.")

            if user_type not in list(user.user_type):
                raise serializers.ValidationError("Invalid user type.")

            refresh = self.get_token(user, user_type)

            data = {}
            data["refresh"] = str(refresh)
            data["access"] = str(refresh.access_token)
            data["user"] = UserSerializer(user).data
            user.last_login = datetime.now()
            user.save()
            return data

        raise serializers.ValidationError("Email and password are required.")
