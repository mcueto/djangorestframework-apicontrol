from random import randrange
from logging import getLogger
from . import models

logger = getLogger(__name__)


def get_current_app_from_request(request):
    try:
        api_key = request.META["HTTP_API_KEY"]
        app = models.App.objects.get(api_key=api_key, enabled=True)
        return app or None

    except Exception as e:
        logger.error(e)
        return None
