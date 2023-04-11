from django.urls import path, include
from .views import (
    EventViewSet,
    ProductListingViewSet,
)

urlpatterns = [
    path("", EventViewSet.as_view({"get": "list", "post": "create"}), name="events"),
    path(
        "<int:pk>/",
        EventViewSet.as_view(
            {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
        ),
        name="event",
    ),
    path(
        "product-listings/",
        ProductListingViewSet.as_view({"get": "list", "post": "create"}),
        name="product-listings",
    ),
    path(
        "product-listing/<int:pk>/",
        ProductListingViewSet.as_view(
            {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
        ),
        name="product-listing-detail",
    ),
]
