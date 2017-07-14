"""API Control Django admin."""
from django.contrib import admin
from .models import (
    Responsible,
    App,
    OrganizationalUnitType,
    OrganizationalUnit
)


class AppAdmin(admin.ModelAdmin):
    """Django admin definition for App Model."""

    readonly_fields = ('api_key',)


admin.site.register(Responsible)
admin.site.register(App, AppAdmin)
admin.site.register(OrganizationalUnitType)
admin.site.register(OrganizationalUnit)
