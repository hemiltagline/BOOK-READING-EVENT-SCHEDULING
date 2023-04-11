from django.urls import path, include
from .views import EventViewSet

urlpatterns = [
    path("", EventViewSet.as_view({"get": "list", "post": "create"}), name="events"),
    path(
        "<int:pk>/",
        EventViewSet.as_view(
            {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
        ),
        name="event",
    ),
]
