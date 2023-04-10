from django.contrib import admin
from books.models import Book, Genre, Product

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Product)
