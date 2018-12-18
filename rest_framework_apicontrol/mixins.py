"""rest_framework_apicontrol model mixins."""
import uuid
from django.db import models
from django.utils import timezone

# Fields constants
STATUS_FIELD_MAX_LENGTH = 32

# Model instances status field choices
MODEL_INSTANCE_STATUS_CHOICES = (
    ('active', 'active'),
    ('inactive', 'inactive'),
    ('archived', 'archived'),
    ('removed_by_user', 'removed_by_user'),
    ('removed_by_admin', 'removed_by_admin'),
    ('removed_automatically', 'removed_automatically'),
)


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
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        abstract = True


class StatusModelMixin(models.Model):
    """
    StatusModelMixin.

    It's a model mixin to set an status to a Model Instance.
    """

    status = models.CharField(
        max_length=STATUS_FIELD_MAX_LENGTH,
        choices=MODEL_INSTANCE_STATUS_CHOICES,
        default='active'
    )

    def activate_status(self, obj, commit=True):
        """Activate the instance."""
        obj.status = 'active'

        if commit:
            obj.save()

    def deactivate_status(self, obj, commit=True):
        """Deactivate the instance."""
        obj.status = 'inactive'

        if commit:
            obj.save()

    def archive_status(self, obj, commit=True):
        """Archive the instance."""
        obj.status = 'archived'

        if commit:
            obj.save()

    # The following statuses are not implemented as functions(maybe in the
    # future if needed):
    # 'removed_by_user'
    # 'removed_by_admin'
    # 'removed_automatically'

    class Meta:
        abstract = True


class TrackableModelMixin(models.Model):
    """
    TrackableModelMixin.

    It's a model mixin to track when a model instance is created
    or updated.
    """

    created_at = models.DateTimeField(
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        default=timezone.now
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
