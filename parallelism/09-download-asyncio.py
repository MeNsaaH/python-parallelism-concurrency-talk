"""
`asyncio.Task` is also an subclass of Future designed to wrap a coroutine
in asyncio, `yield from` is used to give control back to the event loop
the `yield from` is the coroutine equivalent of `add_done_callback`
as PEP492, asyncio introduced the `async` and `await` for the `coroutine` and
`yield from` functions respectively
`async` strictlys define coroutines and separate it from generators
hence removing the `__iter__` and `__next__` implementations and can be inspected
with `inspect.iscoroutine()` function
`await` acts like `yield from` but it is only applicable to `awaitable` objects
which is an object that defines the `__await__()` method that returns an iterator
which is not a coroutine itself
"""

import asyncio
import dis

import aiohttp
import async_timeout

from download_sync import BASE_URL, main, save_img, show

# # Check out the difference in implementation
# @asyncio.coroutine
# def python_coro(x):
#     yield from x

# async def python_async(x):
#     await x

# dis.dis(python_coro)
# print('\n\n')
# dis.dis(python_async)


# @asyncio.coroutine
# def get_img(cc):
#     url = '{}/{cc}/'.format(BASE_URL, cc=cc.lower())
#     resp = yield from aiohttp.request('GET', url)
#     image = yield from resp.read()
#     return image


# the async function is the equivalent of the @asyncio.coroutine for
# previous python versions before 3.5

async def download_one(cc):
    url = '{}{cc}.jpg'.format(BASE_URL, cc=cc.lower())
    async with aiohttp.ClientSession() as session:
        image = await get_img(session, url)
    show(cc)
    save_img(image, cc.lower() + '.jpg')
    return cc

def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)

async def get_img(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.read()




if __name__ == '__main__':
 main(download_many)
