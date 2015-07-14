"""
catimg

Uses iTerm2's proprietary escape codes and Imgur to display an image of a cat
in your terminal.

NOTE: I do not own the images that you see, nor have I any control over
them. You will see some image that is tagged as "cat" on Imgur. That could be
anything. We do filter out images that are tagged NSFW, but there are no
guarantees that you won't see something you wish you hadn't. Use at your own
risk.

License: MIT

"""
import sys
import argparse

from .iterm2 import iterm2_display_image_file
from .imgur import update_img_cache, get_random_image

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--files', nargs='+', metavar='IMAGES', default=(),
                   help='Files to display')
    parser.add_argument('--verbose', action='store_true', help="Show verbose output")
    parser.add_argument('--update-cache', action='store_true', help="Update the image cache and exit")
    parser.add_argument('--no-download', action='store_false', dest='download', default=True, help="Don't download anything from the internet")
    parser.add_argument('--no-delete', action='store_false', dest='delete',
    default=True, help="Don't delete old images")

    args = parser.parse_args()

    for img in args.files:
        iterm2_display_image_file(img)
        print()
    if not args.files:
        if args.update_cache:
            update_img_cache(verbose=args.verbose)
            return
        image = get_random_image(verbose=args.verbose)
        if not image and args.download:
            print("No cat images found, downloading...")
            update_img_cache(verbose=args.verbose)
            image = get_random_image(delete=args.delete, verbose=args.verbose)
        if image:
            iterm2_display_image_file(image)

if __name__ == '__main__':
    sys.exit(main())
