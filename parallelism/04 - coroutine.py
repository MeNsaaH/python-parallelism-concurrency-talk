""" Simple Coroutine Python """


from collections import namedtuple
# run and inspect coroutine
# A coroutine is only good enough it has entered the running state and can receive values
# A functin generator can be used to prime the coroutine for usage
from functools import wraps
# Special sets of generators with the .send and .next key properties
# A coroutine gets suspended at the right side of yield expression waiting
from inspect import getgeneratorstate
# Coroutines
# for the next time A value is sent to it.
# Performs like a async function
from time import sleep


def coroutine(func):
    """ Decorator: primes 'func' by advancing first yield """
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def simple_coroutine():
    print("-> Coroutine has started")
    # Operation is suspended at yield until next send
    # Whatever is on the right side of gets returned
    # Whatever is on the left get initialized on the next send
    x = yield
    print("-> Coroutine received ", x)


# Start the coroutine
# Prepare for the next send
# Send values to the coroutine
# The stopIteration Exception indicates the end of a coroutine
# and the generator.close function is called

# A coroutine can be in four states:-> created, running, suspended or closed
# The states can be monitored using the inspect getgenerator State
# from inspect import getgeneratorstate


# Repeat previous examples with coroutine generators
# How to return values from coroutine in exception

if __name__ == '__main__':
    # my_coro = simple_coroutine()
    # print(getgeneratorstate(my_coro))
    # next(my_coro)
    # print(getgeneratorstate(my_coro))
    # sleep(3)
    # my_coro.send(5)
    # print(getgeneratorstate(my_coro))

    x = simple_coroutine()
    x.send(20)
