import jwt
from rest_framework import serializers
from rest_framework import status


def OrganizerPermission(request):
    token = request.auth
    if token:
        decoded_token = jwt.decode(str(token), options={"verify_signature": False})
        if decoded_token["user_type"] == "ORGANIZER":
            pass
        else:
            raise serializers.ValidationError({"detail": "Not permission"})


def CustomerPermission(request):
    token = request.auth
    if token:
        decoded_token = jwt.decode(str(token), options={"verify_signature": False})
        if decoded_token["user_type"] == "CUSTOMER":
            pass
        else:
            raise serializers.ValidationError({"detail": "Not permission"})
