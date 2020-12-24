"""API Control Django admin."""
from django.contrib import admin
from .models import (
    Responsible,
    App,
    OrganizationalUnitType,
    OrganizationalUnit,
    LoggingGroup,
    LoggingEvent,
)


class AppAdmin(admin.ModelAdmin):
    """Django admin definition for App Model."""

    readonly_fields = ('api_key',)


class TrackableModelAdmin(admin.ModelAdmin):
    """Django admin definition for Trackable models."""
    readonly_fields = ('created_at', 'updated_at')


# App
admin.site.register(Responsible)
admin.site.register(App, AppAdmin)

# Company hierarchy
admin.site.register(OrganizationalUnitType)
admin.site.register(OrganizationalUnit)

# Logging
admin.site.register(LoggingGroup)
admin.site.register(LoggingEvent)
