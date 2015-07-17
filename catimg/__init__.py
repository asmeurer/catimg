"""
catimg

Uses iTerm2's proprietary escape codes and Imgur to display an image of a cat
in your terminal.

NOTE: I do not own the images that you see, nor have I any control over
them. You will see some image that is tagged as "cat" on Imgur. That could be
anything. I do filter out images that are tagged NSFW, but there are no
guarantees that you won't see something you wish you hadn't. Use at your own
risk.

License: MIT

"""
from .iterm2 import *
from .imgur import *

__version__ = '1.0.2'
