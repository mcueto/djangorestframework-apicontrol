"""API Control models."""
from django.db import models


class Responsible(models.Model):
    """Responsible: person who manage an app or group."""

    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class App(models.Model):
    """App model: One Instance per Client(business or App) that connects."""

    name = models.CharField(max_length=30)
    api_key = models.CharField(max_length=30)
    enabled = models.BooleanField(default=False)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class OrganizationalUnitType(models.Model):
    """Groups type for an App(example: department)."""

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True)
    app = models.ForeignKey(App)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children')

    def __str__(self):
        return self.name


class OrganizationalUnit(models.Model):
    """Group for an App(example: accounting department)."""

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True)
    unit_type = models.ForeignKey(OrganizationalUnitType, related_name="units")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    responsibles = models.ManyToManyField(Responsible)

    def __str__(self):
        return self.name
