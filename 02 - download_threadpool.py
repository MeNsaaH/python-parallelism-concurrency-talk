from concurrent import futures
import os
from download_sync import show, main, save_img, get_img

MAX_WORKERS = 20

def download_one(cc):   
    music = get_img(cc)
    show(cc)
    save_img(music, cc.lower() + '.jpg')
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))   
    with futures.ThreadPoolExecutor(workers) as executor:   
        res = executor.map(download_one, sorted(cc_list))   
    return len(list(res))


if __name__ == '__main__':
    main(download_many)   
