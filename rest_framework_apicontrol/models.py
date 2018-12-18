"""API Control models."""
import uuid
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField
from .mixins import (
    EnabledModelMixin,
    PerAppModelMixin,
    TrackableModelMixin,
    UniqueIDModelMixin,
)
from .utils import (
    generate_random_code,
    get_default_logging_group,
)

# Fields constants
CODE_FIELD_MAX_LENGTH = 128
NAME_FIELD_MAX_LENGTH = 128

# LoggingEvent origin field choices
LOGGING_EVENT_ORIGIN_CHOICES = (
    ('auto', 'auto'),
    ('user', 'user'),
    ('rest', 'rest'),
)


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


class App(EnabledModelMixin, TrackableModelMixin, UniqueIDModelMixin):
    """App model: One Instance per Client(business or App) that connects."""

    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH,
        blank=True
    )
    description = models.TextField(
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
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    metadata = JSONField(
        default=dict,
        blank=True
    )

    def reset_api_key(self, obj, commit=True):
        """Reset the App instance api_key."""
        obj.api_key = uuid.uuid4

        if commit:
            obj.save()

    def __str__(self):
        return self.name


class OrganizationalUnitType(PerAppModelMixin,
                             TrackableModelMixin,
                             UniqueIDModelMixin):
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


class OrganizationalUnit(TrackableModelMixin, UniqueIDModelMixin):
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
        'rest_framework_apicontrol.Responsible'
    )

    def __str__(self):
        return self.name


class LoggingGroup(TrackableModelMixin, UniqueIDModelMixin):
    """Group for a Logging history(example: An model instance on a project)."""
    code = models.CharField(
        max_length=CODE_FIELD_MAX_LENGTH,
        default=generate_random_code
    )
    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH,
        blank=True
    )
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name


class LoggingEvent(TrackableModelMixin, UniqueIDModelMixin):
    """Specific Logging history event(example: An action taken by a user over a model instance)."""

    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH,
        blank=True
    )
    description = models.TextField(
        blank=True
    )
    metadata = JSONField(
        default=dict,
        blank=True
    )
    logging_group = models.ForeignKey(
        LoggingGroup,
        default=get_default_logging_group,
        related_name="events",
        on_delete=models.CASCADE
    )
    origin = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH,
        choices=LOGGING_EVENT_ORIGIN_CHOICES,
        default='auto'
    )

    def __str__(self):
        return self.name
