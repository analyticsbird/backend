from random import randint


def generate_app_id(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return 'x{}'.format(randint(range_start, range_end))