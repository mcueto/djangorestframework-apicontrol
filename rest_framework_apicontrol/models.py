"""API Control models."""
import uuid
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField
from .mixins import (
    PerAppModelMixin,
    TrackableModelMixin,
    UniqueIDModelMixin,
)

# Fields constants
NAME_FIELD_MAX_LENGTH = 128


class Responsible(PerAppModelMixin, TrackableModelMixin, UniqueIDModelMixin):
    """Responsible: person who manage an app or group."""

    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH,
        blank=True,
    )
    email = models.EmailField()

    class Meta:
        unique_together = (
            ("email", "app"),
        )

    def __str__(self):
        return self.email


class App(TrackableModelMixin, UniqueIDModelMixin):
    """App model: One Instance per Client(business or App) that connects."""

    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH,
        blank=True
    )
    logo = models.URLField(
        blank=True,
        null=True
    )
    api_key = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    enabled = models.BooleanField(
        default=False
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    metadata = JSONField()

    def enable(self, obj, commit=True):
        """Enable the App instance."""
        obj.enabled = True

        if commit:
            obj.save()

    def disable(self, obj, commit=True):
        """Disable the App instance."""
        obj.enabled = False

        if commit:
            obj.save()

    def reset_api_key(self, obj, commit=True):
        """Reset the App instance api_key."""
        obj.api_key = uuid.uuid4

        if commit:
            obj.save()

    def __str__(self):
        return self.name


class OrganizationalUnitType(PerAppModelMixin, TrackableModelMixin):
    """Groups type for an App(example: department)."""

    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH
    )
    description = models.TextField(
        blank=True
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class OrganizationalUnit(TrackableModelMixin):
    """Group for an App(example: accounting department)."""

    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH
    )
    description = models.TextField(
        blank=True
    )
    organizational_unit_type = models.ForeignKey(
        OrganizationalUnitType,
        related_name="units",
        on_delete=models.CASCADE
    )
    responsibles = models.ManyToManyField(
        Responsible
    )

    def __str__(self):
        return self.name
