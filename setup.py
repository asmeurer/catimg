#!/usr/bin/env python

import sys
if sys.version_info < (3,):
    sys.exit("catimg requires Python 3")

from setuptools import setup

setup(
    name='catimg',
    version='1.0',
    description='''Print an image of a cat from imgur to iTerm2.''',
    author='Aaron Meurer',
    author_email='asmeurer@gmail.com',
    url='https://github.com/asmeurer/catimg',
    packages=['catimg'],
    package_data={'catimg.tests': ['aloha_cat.png']},
    long_description=open("README.md").read(),
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
