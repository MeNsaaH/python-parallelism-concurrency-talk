""" Let's play with asyncio library some more """

import asyncio
import functools
import time
from threading import Thread

# `asyncio` supports task scheduling using
# call_soon(callback)
# call_soon_threadsafe(callback)
# call_at(when), callback), when => loop.time()
# call_later(delay, callback)

async def do_some_work(x):
    """ Some task to be executed """
    print(f'waiting {x}')
    # returns control to the event loop
    await asyncio.sleep(x)
    print(f"Booyay {x} is done")


# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_some_work(5))

# tasks = [
#     asyncio.ensure_future(do_some_work(5)),
#     asyncio.ensure_future(do_some_work(2)),
# ]

# gather tasks enable task aggregation
# loop.run_until_complete(asyncio.gather(*tasks))

# loop.close()

# We can even execute the tasks on a different thread :)
# The advantage of this method is that work executed by the other event loop
# will not block execution in the current thread.

# def start_event_loop(loop):
#     asyncio.set_event_loop(loop)
#     loop.run_forever()

# async def some_more_work(x):
#     await asyncio.sleep(1)
#     print("More work %s" % x)
#     await asyncio.sleep(x)
#     print("Finished more work %s" % x)

# async def do_work():
#     loop = asyncio.get_event_loop()
#     tasks = [
#         asyncio.ensure_future(do_some_work(5)),
#         asyncio.ensure_future(do_some_work(2)),
#     ]
#     await asyncio.gather(*tasks)

# # notice the `asyncio.new_event_loop` as opposed the `asyncio.get_event_loop`
# new_loop = asyncio.new_event_loop()
# t = Thread(target=start_event_loop, args=(new_loop,))
# t.start()
# future = asyncio.run_coroutine_threadsafe(some_more_work(5), new_loop)
# future2 = asyncio.run_coroutine_threadsafe(do_some_work(2), new_loop)
# print(future.result())
# print(future2.result())
# t.join()

# Scheduling Call back time
# def callback(n, loop):
#     print('callback {} invoked at {}'.format(n, loop.time()))


# async def main(loop):
#     now = loop.time()
#     print('clock time: {}'.format(time.time()))
#     print('loop  time: {}'.format(now))

#     print('registering callbacks')
#     loop.call_at(now + 0.2, callback, 1, loop)
#     loop.call_at(now + 0.1, callback, 2, loop)
#     loop.call_soon(callback, 3, loop)

#     await asyncio.sleep(1)


# event_loop = asyncio.get_event_loop()
# try:
#     print('entering event loop')
#     event_loop.run_until_complete(main(event_loop))
# finally:
#     print('closing event loop')
#     event_loop.close()
