"""
`asyncio.Task` is also an subclass of Future designed to wrap a coroutine
in asyncio, `yield from` is used to give control back to the event loop
the `yield from` is the coroutine equivalent of `add_done_callback`
as PEP492, asyncio introduced the `async` and `await` for the `coroutine` and
`yield from` functions respectively
the async tried to strictly define coroutines and separate it from generators
hence removing the `__iter__` and `__next__` implementations and can be inspected
with `inspect.iscoroutine()` function
"""

# TODO check what the heck is wrong with `async`
# TODO check if `asyncio` now supports HTTP
import asyncio

import aiohttp
import async_timeout

from download_sync import BASE_URL, main, save_img, show

# @asyncio.coroutine
# def get_img(cc):
#     url = '{}/{cc}/'.format(BASE_URL, cc=cc.lower())
#     resp = yield from aiohttp.request('GET', url)
#     image = yield from resp.read()
#     return image


# the async function is the equivalent of the @asyncio.coroutine for
# previous python versions before 3.5
async def get_img(cc):
    url = '{}/{cc}/'.format(BASE_URL, cc=cc.lower())
    resp = await aiohttp.request('GET', url)
    image = await resp.read()
    return image


async def download_one(cc):
    image = await get_img(cc)
    show(cc)
    save_img(image, cc.lower() + '.png')
    return cc

def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)

if __name__ == '__main__':
 main(download_many)
