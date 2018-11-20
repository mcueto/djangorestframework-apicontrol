from random import randrange
from logging import getLogger
from . import models

# generate_random_code
CHARSET = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
DEFAULT_LENGTH = 16
DEFAULT_MAX_TRIES = 32

# get_default_logging_group
DEFAULT_LOGGING_GROUP_CODE='DEFAULT'

logger = getLogger(__name__)


def get_current_app_from_request(request):
    try:
        api_key = request.META["HTTP_API_KEY"]
        app = models.App.objects.get(api_key=api_key, enabled=True)
        return app or None

    except Exception as e:
        logger.error(e)
        return None


def generate_random_code(length=DEFAULT_LENGTH, max_tries=DEFAULT_MAX_TRIES):
    code = ""
    loop_num = 0
    unique = False

    while not unique:
        if loop_num < max_tries:
            new_code = ''
            for i in range(length):
                new_code += CHARSET[randrange(0, len(CHARSET))]
                code = new_code
                unique = True
            loop_num += 1
            return code
        else:
            raise ValueError("Couldn't generate a unique code.")


def get_default_logging_group(code=DEFAULT_LOGGING_GROUP_CODE):
    return models.LoggingGroup.objects.get(code=code).pk
