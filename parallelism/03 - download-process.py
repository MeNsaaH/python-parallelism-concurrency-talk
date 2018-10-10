import os
from concurrent import futures

from download_sync import get_img, main, save_img, show

MAX_WORKERS = 20
# THREAD POOL EXECUTOR
def download_one(cc):
    music = get_img(cc)
    save_img(music, cc.lower() + '.jpg')
    show(cc)
    return cc

# Using Thread pool Executor best for I/O bound Processing

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


# a future has a .done to check if it is done
# .add_done_callback() which is called when the callable is executed
def download_many_(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            # takes a callable and returns a future
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))
        results = []
        # as completed takes a callable iterable and returns an
        # iterator that yields a future when it is done
        for future in futures.as_completed(to_do):
            # get the result of the future
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)
    return len(results)

if __name__ == '__main__':
    main(download_many_)


# Future Provides a high level abstraction of what is actually being
# Handled by the threading library and multiprocessing Library which
# we can implement on our own for more added flexibility.
