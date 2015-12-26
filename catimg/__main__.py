import sys
import argparse

from iterm2_tools import display_image_file
from .imgur import update_img_cache, get_random_image
from . import __version__, __doc__

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-f', '--files', nargs='+', metavar='IMAGES', default=(),
                   help='Files to display')
    parser.add_argument('-v', '--verbose', action='store_true', help="Show verbose output")
    parser.add_argument('-V', '--version', action='version', version='catimg ' + __version__)
    parser.add_argument('--update-cache', action='store_true', help="Update the image cache and exit")
    parser.add_argument('--no-download', action='store_false', dest='download', default=True, help="Don't download anything from the internet")
    parser.add_argument('--no-delete', action='store_false', dest='delete',
    default=True, help="Don't delete old images")

    args = parser.parse_args()

    for img in args.files:
        display_image_file(img)
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
            display_image_file(image)
            print()

if __name__ == '__main__':
    sys.exit(main())
