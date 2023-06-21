from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import models
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django_filters.views import FilterView
from typing import Any
from typing import Optional
from users.filters import UserFilter
from users.forms import UserProfileForm
from users.forms import UserUpdateForm

User = get_user_model()


@method_decorator(login_required, name="dispatch")
class ProfileView(UpdateView):
    template_name = "users/profile.html"
    form_class = UserProfileForm
    success_url = reverse_lazy("profile")

    def get_object(
        self, queryset: Optional[models.query.QuerySet[Any]] = ...
    ) -> models.Model:
        return self.request.user

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, "Profile updated!")
        return super().form_valid(form)


class UserListView(PermissionRequiredMixin, FilterView):
    model = User
    paginate_by = 10
    template_name = "users/list.html"
    permission_required = "is_superuser"
    filterset_class = UserFilter
    context_object_name = "user_list"


class UserUpdateView(PermissionRequiredMixin, UpdateView):

    template_name = "users/update.html"
    form_class = UserUpdateForm
    queryset = User.objects.all()
    success_url = reverse_lazy("users-list")
    permission_required = "is_superuser"
    slug_field = "uuid"
    slug_url_kwarg = "uuid"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, "User updated!")
        return super().form_valid(form)
