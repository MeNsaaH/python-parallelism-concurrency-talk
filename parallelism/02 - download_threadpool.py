import os
from concurrent import futures

from download_sync import get_img, main, save_img, show

MAX_WORKERS = 20

def download_one(cc):
    music = get_img(cc)
    show(cc)
    save_img(music, cc.lower() + '.jpg')
    return cc


# def download_many(cc_list):
#     workers = min(MAX_WORKERS, len(cc_list))
#     # context manager
#     with futures.ThreadPoolExecutor(workers) as executor:
#         res = executor.map(download_one, sorted(cc_list))
#     return len(list(res))


def download_many(cc_list):
    # workers = min(MAX_WORKERS, len(cc_list))
    # Context manager that automatically closes the pool
    # By calling executor._exit__ => executor.shutdown(wait=True)
    # with futures.ThreadPoolExecutor(workers) as executor:
        # the executor.map returns a generator which contains results of exec
        # in the order they were added
        # processPool uses number of cores the CPU has
    with futures.ProcessPoolExecutor() as executor:
        res = executor.map(download_one, sorted(cc_list))
    return len(list(res))


if __name__ == '__main__':
    main(download_many)
