#!/usr/bin/env python

import sys
if sys.version_info < (3,):
    sys.exit("catimg requires Python 3")

from setuptools import setup

setup(
    name='catimg',
    version='1.0.1',
    description='''Print an image of a cat from imgur to iTerm2.''',
    author='Aaron Meurer',
    author_email='asmeurer@gmail.com',
    url='https://github.com/asmeurer/catimg',
    packages=['catimg'],
    package_data={'catimg.tests': ['aloha_cat.png']},
    long_description="""
Uses iTerm2's proprietary escape codes and Imgur to display an image of a cat
in your terminal.

NOTE: I do not own the images that you see, nor have I any control over
them. You will see some image that is tagged as "cat" on Imgur. That could be
anything. I do filter out images that are tagged NSFW, but there are no
guarantees that you won't see something you wish you hadn't. Use at your own
risk.
""",
    entry_points={'console_scripts': [ 'catimg = catimg.__main__:main']},
    install_requires=[
        'requests',
        'imgurpython',
    ],
    license="MIT",
    classifiers=[
        'Environment :: MacOS X',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',
        ],
)
