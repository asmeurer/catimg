import sys
import os

from requests import Session

from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from imgurpython.imgur.models.gallery_album import GalleryAlbum
from .util import human_bytes

CLIENT_ID = "6efbafee90d77dc"
CLIENT_SECRET = "d0e87b8e5ec48cb345380f6fbcaf2ff70167755c"

CATIMG_DIR = os.path.expanduser('~/.catimg')
IMG_CACHE = os.path.join(CATIMG_DIR, 'cache')
# client = ImgurClient(CLIENT_ID, CLIENT_SECRET)

def update_img_cache(verbose=False):
    try:
        client = ImgurClient(CLIENT_ID, CLIENT_SECRET)
        if verbose:
            print("Getting Imgur images")
        items = client.gallery_tag('cat')
        s = Session()
        os.makedirs(IMG_CACHE, exist_ok=True)
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

            print("Downloading %s (%s)" % (item.link, human_bytes(item.size)))
            r = s.get(item.link)

            if verbose:
                print("Writing %s" % path)
            with open(path, 'wb') as f:
                f.write(r.content)

    except ImgurClientError as e:
        print("Error: Could not get new images (%s)" % e, file=sys.stderr)
