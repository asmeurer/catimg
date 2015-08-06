#!/usr/bin/env python

import sys
if sys.version_info < (3,):
    sys.exit("catimg requires Python 3")

from setuptools import setup
import versioneer

setup(
    name='catimg',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='''Print an image of a cat from Imgur to iTerm2.''',
    author='Aaron Meurer',
    author_email='asmeurer@gmail.com',
    url='https://github.com/asmeurer/catimg',
    packages=['catimg'],
    long_description="""
catimg

Uses iTerm2's proprietary escape codes and Imgur to display an image of a cat
in your terminal.

NOTE: I do not own the images that you see, nor have I any control over
them. You will see some image that is tagged as "cat" on Imgur. That could be
anything. I do filter out images that are tagged NSFW, but there are no
guarantees that you won't see something you wish you hadn't. Use at your own
risk.

License: MIT

""",
    entry_points={'console_scripts': [ 'catimg = catimg.__main__:main']},
    install_requires=[
        'requests',
        'imgurpython',
        'iterm2-tools>=2.0',
    ],
    license="MIT",
    classifiers=[
        'Environment :: MacOS X',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',
        ],
    zip_safe=False,
)
