from .manager import UserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None

    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(_("name"), max_length=256, null=True, blank=True)
    avatar = models.ImageField(_("avatar"), upload_to="avatars", null=True, blank=True)

    force_change_password = models.BooleanField(
        _("force change password"), default=False
    )
    date_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
