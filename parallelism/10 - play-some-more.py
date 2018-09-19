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

def start_event_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def some_more_work(x):
    print("More work %s" % x)
    await asyncio.sleep(x)
    print("Finished more work %s" % x)

# notice the `asyncio.new_event_loop` as opposed the `asyncio.get_event_loop`
new_loop = asyncio.new_event_loop()
t = Thread(target=start_event_loop, args=(new_loop,))
t.start()
new_loop.call_soon_threadsafe(some_more_work, 6)
new_loop.call_soon_threadsafe(do_some_work, 3)
# future = asyncio.run_coroutine_threadsafe(some_more_work(5), new_loop)
# future2 = asyncio.run_coroutine_threadsafe(do_some_work(2), new_loop)
# print(future.result())
# print(future2.result())
t.join()
