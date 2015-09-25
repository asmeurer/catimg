# catimg

Print an image of a cat from imgur to iTerm2.

![](example.png)

Uses iTerm2's [proprietary escape codes](https://iterm2.com/images.html) and
Imgur to display an image of a cat in your terminal.

NOTE: I do not own the images that you see, nor have I any control over
them. You will see some image that is tagged as "cat" on Imgur. That could be
anything. I do filter out images that are tagged NSFW, but there are no
guarantees that you won't see something you wish you hadn't. Use at your own
risk.

SECOND NOTE: This requires iTerm2 2.9 or later (i.e., at the time of this
writing, at least the beta release). The beta release is quite stable in my
experience. You can download it
[here](https://www.iterm2.com/downloads.html).

# Installation

catimg depends on [requests](http://docs.python-requests.org/en/latest/),
[imgurpython](https://github.com/Imgur/imgurpython),
[iterm2-tools](https://github.com/asmeurer/iterm2-tools) and
[iTerm2](https://iterm2.com/).  It depends on Python 3 (it will not work in
Python 2).

The easiest way to install it is with pip

    pip install catimg

or conda

    conda install -c asmeurer catimg

# License

MIT
