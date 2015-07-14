"""
catimg

Uses iTerm2's proprietary escape codes and Imgur to display an image of a cat
in your terminal.

NOTE: I do not own the images that you see, nor have I any control over
them. You will see some image that is tagged as "cat" on Imgur. That could be
anything. Use at your own risk.

License: MIT
"""
import sys
import argparse

from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError

from catimg.iterm2 import iterm2_display_image_file
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--files', nargs='+', metavar='IMAGES',
                   help='Files to display')

    args = parser.parse_args()
    for img in args.files:
        iterm2_display_image_file(img)
        print()

if __name__ == '__main__':
    sys.exit(main())
