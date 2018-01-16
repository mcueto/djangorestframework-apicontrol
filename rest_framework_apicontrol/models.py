"""API Control models."""
import uuid
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField
from .mixins import (
    TrackableModelMixin,
)


class Responsible(TrackableModelMixin):
    """Responsible: person who manage an app or group."""

    name = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    email = models.EmailField(
        unique=True
    )

    def __str__(self):
        return self.email


class App(TrackableModelMixin):
    """App model: One Instance per Client(business or App) that connects."""

    name = models.CharField(
        max_length=30
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

    def __str__(self):
        return self.name


class OrganizationalUnitType(TrackableModelMixin):
    """Groups type for an App(example: department)."""

    name = models.CharField(
        max_length=30
    )
    description = models.CharField(
        max_length=30,
        blank=True
    )
    app = models.ForeignKey(
        App,
        on_delete=models.CASCADE
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
        max_length=30
    )
    description = models.CharField(
        max_length=30,
        blank=True
    )
    unit_type = models.ForeignKey(
        OrganizationalUnitType,
        related_name="units",
        on_delete=models.CASCADE
    )
    responsibles = models.ManyToManyField(
        Responsible
    )

    def __str__(self):
        return self.name
