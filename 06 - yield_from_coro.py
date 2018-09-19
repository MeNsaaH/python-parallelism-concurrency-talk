""" Understanding Coroutines and Generators using sub-generators"""

from collections import namedtuple

from coroutil import coroutine

Result = namedtuple('Result', 'count average')


# The difference between `yield` and `yield from`
# `yield from ` yields from a set of iterators when used in a generator
# It also allows delegating returns to a sub-generator
# it does not need special error handling to get return values

# The subgenerator 
def averager():
    """ coroutine for calculating cumulative average """
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        # the terminating condition
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    # This is will be the value of the `yield from` in the delegator
    # This will be sent directly to the caller
    return Result(count, average)


# the delegating generator
@coroutine
def grouper(results, key):
    """ the delegating generator """ 
    while True:
        # Each iteration creates a new instance of the subgenerator
        # each a generator operating as a coroutine
        # The delegator suspends here as long as the subgenerator
        # keeps receiving input from the main caller 
        # upon return a new instance is created
        # the subgenerator here is automatically primed
        results[key] = yield from averager()


# The main caller or the client code
def main_caller(data):
    """ the client code, a.k.a. the caller """
    results = {}
    for key, values in data.items():
        # creates a primed coroutine
        group = grouper(results, key)
        # values are sent to the subgenerator
        # the grouper doesn't have a chance to process the inputs
        for value in values:
            group.send(value)
        # terminates the grouper allowing for another instance of averager
        # to be created
        group.send(None)
    report(results)

def report(results):
    """ results generstor """
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
              result.count, group, result.average, unit))
data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == '__main__':
    main_caller(data)
