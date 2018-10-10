""" Understanding Coroutines and Generators """

from collections import namedtuple
from functools import wraps

from coroutil import coroutine

Result = namedtuple('Result', 'count average')
# A simple Coroutine the calculates the Running Average
@coroutine
def averager():
    """ coroutine for calculating cumulative average """
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        print(f"{term} has being received for number {count}")
        average = total/count
    return Result(count, average)
