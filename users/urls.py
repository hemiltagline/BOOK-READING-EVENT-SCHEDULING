from django.urls import path
from users.views import UserViewSet, UserCreateView, UserDeleteView

urlpatterns = [
    # path("sign-in/", admin.site.urls),
    # path("sign-up/", include("users.urls")),
    path(
        "users/", UserViewSet.as_view({"get": "list", "post": "create"}), name="users"
    ),
    path(
        "user/<int:pk>/",
        UserViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="user",
    ),
    path("sign-up/", UserCreateView.as_view(), name="create-user"),
    path("user/<int:pk>/", UserDeleteView.as_view(), name="user_delete"),
]
