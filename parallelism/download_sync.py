import os
import sys
import time

import requests

BASE_URL = r'https://www.google.com.ng/search?q='
DEST_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'downloads'
)
POP20_CC = ('A B C D E F G H I J K L M N AA BB CC DD EE FF GG HH II JJ KK LL MM NN').split()

def save_img(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_img(cc):
    # Use requests to retreive light weight files
    url = '{}{cc}.jpg'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):
    for cc in sorted(cc_list):
        img = get_img(cc)
        save_img(img, cc.lower() + '.jpg')
        show(cc)
    return len(cc_list)

def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} songs downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)
