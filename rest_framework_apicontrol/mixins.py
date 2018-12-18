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

    def activate(self, commit=True):
        """Activate the instance."""
        self.active = True

        if commit:
            self.save()

    def deactivate(self, commit=True):
        """Deactivate the instance."""
        self.active = False

        if commit:
            self.save()

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

    def enable(self, commit=True):
        """Enable the instance."""
        self.enabled = True

        if commit:
            self.save()

    def disable(self, commit=True):
        """Disable the instance."""
        self.enabled = False

        if commit:
            self.save()

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


class InstanceStatusModelMixin(models.Model):
    """
    InstanceStatusModelMixin.

    It's a model mixin to set an status to a Model Instance.
    """

    instance_status = models.CharField(
        max_length=STATUS_FIELD_MAX_LENGTH,
        choices=MODEL_INSTANCE_STATUS_CHOICES,
        default='active'
    )

    def activate_instance(self, commit=True):
        """Activate the instance."""
        self.instance_status = 'active'

        if commit:
            self.save()

    def deactivate_instance(self, commit=True):
        """Deactivate the instance."""
        self.instance_status = 'inactive'

        if commit:
            self.save()

    def archive_instance(self, commit=True):
        """Archive the instance."""
        self.instance_status = 'archived'

        if commit:
            self.save()

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
