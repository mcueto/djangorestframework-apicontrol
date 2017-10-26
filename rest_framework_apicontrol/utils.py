from random import randrange
from logging import getLogger
from .models import App

logger = getLogger(__name__)


CHARSET = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
LENGTH = 16
MAX_TRIES = 32


code = ""

def generate_code():
    loop_num = 0
    unique = False

    while not unique:
        if loop_num < MAX_TRIES:
            new_code = ''
            for i in range(LENGTH): # TODO: change to xrange() for python 2
                new_code += CHARSET[randrange(0, len(CHARSET))]
                code = new_code
                unique = True
            loop_num += 1
            return new_code
        else:
            raise ValueError("Couldn't generate a unique code.")


def get_current_app_by_request(request):
    try:
        api_key = request.META["HTTP_API_KEY"]
        app = App.objects.get(api_key=api_key, enabled=True)
        return app or None

    except Exception as e:
        logger.error(e)
        return None
