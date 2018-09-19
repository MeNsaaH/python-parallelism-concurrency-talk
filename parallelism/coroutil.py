from functools import wraps
from collections import namedtuple

def coroutine(func):
    """ Decorator: primes 'func' by advancing first yield """
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer
