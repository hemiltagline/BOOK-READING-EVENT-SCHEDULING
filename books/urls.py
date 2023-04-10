from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, GenreDetail, BookList, BookDetail

urlpatterns = [
    path("genre/", GenreViewSet.as_view(), name="genre-list"),
    path("genre/<int:pk>/", GenreDetail.as_view(), name="genre"),
    path("", BookList.as_view(), name="book-list"),
    path("<int:pk>/", BookDetail.as_view(), name="book-detail"),
]
