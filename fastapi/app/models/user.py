from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseModelMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
        self, username: str, email: str, password: str, **extra_fields: dict
    ) -> "User":
        """Create and save a user with the given username, email, and
        password."""
        if not username:
            raise ValueError("The given username must be set.")

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(  # type: ignore
        self, username: str, email: str, password: str, **extra_fields
    ) -> "User":
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(  # type: ignore
        self, username: str, email: str, password: str, **extra_fields
    ) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, BaseModelMixin):
    objects = UserManager()

    email = models.EmailField(_("email address"), unique=True)

    MIN_LENGTH_USERNAME = 1
    MAX_LENGTH_USERNAME = 20
    username = models.CharField(
        _("username"),
        max_length=MAX_LENGTH_USERNAME,
    )

    # permissions
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ["-created_at"]
