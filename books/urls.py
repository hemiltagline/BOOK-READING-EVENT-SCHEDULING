from django.urls import path, include
from .views import (
    GenreDetail,
    BookDetail,
    ProductDetail,
)

urlpatterns = [
    path(
        "genre/",
        GenreDetail.as_view({"get": "list", "post": "create"}),
        name="genre-list",
    ),
    path(
        "genre/<int:pk>/",
        GenreDetail.as_view(
            {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
        ),
        name="genre",
    ),
    path("", BookDetail.as_view({"get": "list", "post": "create"}), name="book-list"),
    path(
        "<int:pk>/",
        BookDetail.as_view(
            {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
        ),
        name="book-detail",
    ),
    path(
        "product/",
        ProductDetail.as_view({"get": "list", "post": "create"}),
        name="genre-list",
    ),
    path(
        "product/<int:pk>/",
        ProductDetail.as_view(
            {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
        ),
        name="genre",
    ),
]
