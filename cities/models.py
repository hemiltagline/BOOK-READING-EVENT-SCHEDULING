from django.db import models
from backend.models import BaseModel


class CitiesPage(BaseModel):
    city_name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.city_name
