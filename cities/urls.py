from django.urls import path
from .views import CitiesPageViewSet

urlpatterns = [
    path(
        "", CitiesPageViewSet.as_view({"get": "list", "post": "create"}), name="cities"
    ),
    path(
        "<int:pk>/",
        CitiesPageViewSet.as_view(
            {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
        ),
        name="get_update_delete_city",
    ),
]
