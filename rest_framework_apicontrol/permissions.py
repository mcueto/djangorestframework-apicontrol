"""API Control permissions."""
from __future__ import unicode_literals
from logging import getLogger
from rest_framework.permissions import BasePermission
from .models import App

logger = getLogger(__name__)


class HasApiKeyPermission(BasePermission):
    """Allow request only when the header has a valid api_key."""

    def has_permission(self, request, view):
        """Validate if an App with the Api-Key header exists and is enabled."""
        if request.method == 'OPTIONS':
            return True

        try:
            api_key = request.META["HTTP_API_KEY"]
            app = App.objects.get(api_key=api_key, enabled=True)
            if(app):
                return True

        except Exception as e:
            logger.error(e)
            return False
