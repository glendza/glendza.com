from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        blank=True,
        unique=True,
    )

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
