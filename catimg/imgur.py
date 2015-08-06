import sys
import os
import random
import time

from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

from requests import Session

from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from imgurpython.imgur.models.gallery_album import GalleryAlbum

from .util import human_bytes

CLIENT_ID = "6efbafee90d77dc"
CLIENT_SECRET = "d0e87b8e5ec48cb345380f6fbcaf2ff70167755c"

CATIMG_DIR = os.path.expanduser('~/.catimg')
USAGES_FILE = os.path.join(CATIMG_DIR, 'usages')
IMG_CACHE = os.path.join(CATIMG_DIR, 'cache')
LOCK_PATH = os.path.join(CATIMG_DIR, 'lock')
RETRIES = 10
# client = ImgurClient(CLIENT_ID, CLIENT_SECRET)

def _download_and_write(item, path, session, verbose=False):
    print("Downloading %s (%s)" % (item.link, human_bytes(item.size)))
    r = session.get(item.link)

    if verbose:
        print("Writing %s" % path)
    with open(path, 'wb') as f:
        f.write(r.content)

def update_img_cache(verbose=False):
    try:
        os.makedirs(LOCK_PATH)
    except OSError:
        if verbose:
            print("Another process is downloading cat images.")
        return

    try:
        client = ImgurClient(CLIENT_ID, CLIENT_SECRET)
        if verbose:
            print("Getting Imgur images")
        items = client.gallery_tag('cat')
        session = Session()
        os.makedirs(IMG_CACHE, exist_ok=True)
        to_download = {}
        for item in items.items:
            fn = item.link.rsplit('/', 1)[1]
            path = os.path.join(IMG_CACHE, fn)

            if item.nsfw:
                if verbose:
                    print("%s is NSFW, skipping" % item.link)
                continue
            if isinstance(item, GalleryAlbum):
                if verbose:
                    print("%s is an album, skipping" % item.link)
                continue
            if os.path.exists(path):
                if verbose:
                    print("%s already exists, skipping" % path)
                continue
            to_download[item] = path

        with ThreadPoolExecutor(10) as executor:
            for item, path in to_download.items():
                executor.submit(_download_and_write, item, path, session,
            verbose=verbose)

    except ImgurClientError as e:
        print("Error: Could not get new images (%s)" % e, file=sys.stderr)
    finally:
        try:
            os.rmdir(LOCK_PATH)
        except FileNotFoundError:
            pass

def get_random_image(n=3, delete=True, verbose=False):
    """
    Get a random image, which hasn't been used more than n times. Usages are
    stored on disk.

    If delete=True, delete files that have been used more than n times.

    Returns the file path, or None if no files could be found.
    """
    for i in range(RETRIES):
        try:
            os.makedirs(LOCK_PATH)
            break
        except OSError:
            if verbose:
                print("Another process is getting a cat image. Retrying in %s milliseconds." % 2**i*10)
                time.sleep(2**i/100)
    else:
        if verbose:
            print("Could not get lock after %s retries. Giving up." % RETRIES)
        return

    try:
        if verbose:
            print("Max usage:", n)
        usages = defaultdict(int)
        os.makedirs(IMG_CACHE, exist_ok=True)
        if os.path.exists(USAGES_FILE):
            with open(USAGES_FILE, 'r') as f:
                for line in f.read().splitlines():
                    usages.update({img: int(uses) for img, uses in [line.split()]})

        if verbose:
            print("Usages:", usages)

        files = os.listdir(IMG_CACHE)
        usable_files = {f for f in files if usages[f] < n}
        if verbose:
            print("Usable files:", usable_files)

        if not usable_files:
            return None

        random_file = random.choice(list(usable_files))
        if verbose:
            print("Random file:", random_file)
        usages[random_file] += 1

        if delete:
            # Shouldn't delete the random_file
            unusable_files = set(files) - usable_files
            for f in unusable_files:
                if verbose:
                    print("Removing %s" % os.path.join(IMG_CACHE, f))
                os.remove(os.path.join(IMG_CACHE, f))

        if verbose:
            print("New usages:", usages)
            print("Writing usages to %s" % USAGES_FILE)
        with open(USAGES_FILE, 'w') as f:
            f.write('\n'.join(' '.join([img, str(usages[img])]) for img in usages))

        return os.path.join(IMG_CACHE, random_file)
    finally:
        try:
            os.rmdir(LOCK_PATH)
        except FileNotFoundError:
            pass
