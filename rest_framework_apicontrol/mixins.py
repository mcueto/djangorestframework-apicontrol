"""rest_framework_apicontrol model mixins."""
import uuid
from django.db import models


class ActiveModelMixin(models.Model):
    """
    ActiveModelMixin.

    It's a model mixin to set if a model instance is active or not.
    """

    active = models.BooleanField(
        default=False
    )

    def activate(self, obj, commit=True):
        """Activate the instance."""
        obj.enabled = True

        if commit:
            obj.save()

    def deactivate(self, obj, commit=True):
        """Deactivate the instance."""
        obj.enabled = False

        if commit:
            obj.save()

    class Meta:
        abstract = True


class EnabledModelMixin(models.Model):
    """
    EnabledModelMixin.

    It's a model mixin to set if a model instance is enabled or not.
    """

    enabled = models.BooleanField(
        default=False
    )

    def enable(self, obj, commit=True):
        """Enable the instance."""
        obj.enabled = True

        if commit:
            obj.save()

    def disable(self, obj, commit=True):
        """Disable the instance."""
        obj.enabled = False

        if commit:
            obj.save()

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
