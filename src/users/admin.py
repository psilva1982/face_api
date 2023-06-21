from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            _("Personal info"),
            {
                "fields": (
                    "email",
                    "name",
                    "avatar",
                    "password",
                    "force_change_password",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "date_joined",
                    "last_login",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    list_display = ["id", "date_joined", "email", "name", "is_staff"]
    list_filter = ["is_staff", "is_superuser", "is_active", "groups"]
    search_fields = ["email", "name"]
    ordering = ["email"]
    readonly_fields = ["date_joined", "last_login"]
