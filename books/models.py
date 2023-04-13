from django.db import models
from backend.models import BaseModel


class Genre(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="product_images/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Book(BaseModel):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, null=True, related_name="book"
    )
    summary = models.TextField(max_length=1000)
    cover_image = models.ImageField(
        upload_to="book_covers/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
