from random import randrange

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
