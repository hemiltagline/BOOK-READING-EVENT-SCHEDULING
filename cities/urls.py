from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CitiesPageViewSet, CityDetail

router = DefaultRouter()
router.register(r"", CitiesPageViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("<int:pk>/", CityDetail.as_view(), name="get_update_delete_city"),
]
