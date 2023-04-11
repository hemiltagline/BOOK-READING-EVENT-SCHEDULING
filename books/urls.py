from django.urls import path, include
from .views import (
    GenreViewSet,
    GenreDetail,
    BookList,
    BookDetail,
    ProductList,
    ProductDetail,
)

urlpatterns = [
    path("genre/", GenreViewSet.as_view(), name="genre-list"),
    path("genre/<int:pk>/", GenreDetail.as_view(), name="genre"),
    path("", BookList.as_view(), name="book-list"),
    path("<int:pk>/", BookDetail.as_view(), name="book-detail"),
    path("product/", ProductList.as_view(), name="genre-list"),
    path("product/<int:pk>/", ProductDetail.as_view(), name="genre"),
]
