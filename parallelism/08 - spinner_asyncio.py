import asyncio
import itertools
import sys

# Asyncio uses a stricter definition `coroutine` to achieve concurrency
# Asyncio uses `cooperative multitasking` to achieve multitasking
# `coroutine` used for asyncio must `yield from` and not `yield` in its body
# The caller must as well invoke the coroutine with a `yield from` or passing
# the function to an `asyncio` function such as `asyncio.create_task`
# Coroutines should be decorated with the `asyncio.coroutine` decorator recommended
# the decorator is not a priming decorator. It helps with debugging by issuing
# a warning when a coroutine is garbage collected without being yielded from
# TODO look up the async library
# A task must be registered with an event_loop before it can be executed


@asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            # Use `asyncio.sleep` instead of `time.sleep` to prevent
            # blocking the event loop
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():
    # pretend waiting a long time for I/O
    yield from asyncio.sleep(3)
    return 42


@asyncio.coroutine
def supervisor():
    # schedules the spin in a task object which returns immediately
    # `asyncio.Task` is roughly the equivalent of `threading.Thread`
    # a `Task` drives a coroutine, a `Thread` invokes a callable
    # a `Task` instance is scheduled to run while the `Thread` must be
    # explicitly told to run. With threads, locks are held to synchronise
    # operations with multiple threads. With coroutines, everything is protected
    # from interruptions by default. a coroutine can only be cancelled when
    # it is suspended at a `yield` or `yield ` point
    spinner = asyncio.create_task(spin('thinking!'))
    print('spinner object:', spinner)
    # does not block the event loop
    result = yield from slow_function()
    # cancelling a task object raises an `asyncio.CancelledError`
    spinner.cancel()
    return result


def main():
    # get reference to the event loop which is the current event loop
    # the python program is running on
    loop = asyncio.get_event_loop()
    # drive the supervisor coroutine to completion
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
