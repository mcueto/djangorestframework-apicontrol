"""rest_framework_apicontrol model mixins."""
import uuid
from django.db import models


class TrackableModelMixin(models.Model):
    """
    TrackableModelMixin.

    It's a model mixin to track when a model instance is created
    or updated.
    """

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class UniqueIDModelMixin(models.Model):
    """
    UniqueIDModelMixin.

    It's a model mixin to set the model unique_id field as an UUIDField with
    UUID4 algorithm.
    """

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        abstract = True


class PerAppModelMixin(models.Model):
    """
    PerAppModelMixin.

    It's a model mixin that allows a model to be associated with an app.
    """

    app = models.ForeignKey(
        'rest_framework_apicontrol.app',
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True
