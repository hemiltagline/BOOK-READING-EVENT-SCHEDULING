from django.urls import path
from users.views import UserViewSet

urlpatterns = [
    # path("sign-in/", admin.site.urls),
    # path("sign-up/", include("users.urls")),
    path(
        "users/", UserViewSet.as_view({"get": "list", "post": "create"}), name="users"
    ),
    path(
        "user/<int:id>/",
        UserViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="user",
    ),
]
