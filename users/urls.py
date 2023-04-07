from django.urls import path
from users.views import UserViewSet, UserCreateView, UserDeleteView, UserLoginView

urlpatterns = [
    path("sign-up/", UserCreateView.as_view(), name="create-user"),
    path("sign-in/", UserLoginView.as_view(), name="login-user"),
    path(
        "users/", UserViewSet.as_view({"get": "list", "post": "create"}), name="users"
    ),
    path(
        "user/<int:pk>/",
        UserViewSet.as_view(
            {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
        ),
        name="user",
    ),
    path("user/<int:pk>/", UserDeleteView.as_view(), name="user_delete"),
]
