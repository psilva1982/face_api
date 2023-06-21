from .views import ProfileView
from .views import UserListView
from .views import UserUpdateView
from django.urls import path

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("list/", UserListView.as_view(), name="users-list"),
    path("<uuid>/edit/", UserUpdateView.as_view(), name="user-edit"),
]
