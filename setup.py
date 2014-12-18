#!/usr/bin/env python

"""
Setup script for puppies.
"""

import setuptools

from puppies import __project__, __version__

import os
if os.path.exists('README.rst'):
    README = open('README.rst').read()
else:
    README = ""  # a placeholder, readme is generated on release
CHANGES = open('CHANGES.md').read()


setuptools.setup(
    name=__project__,
    version=__version__,

    description="puppies is a Python 3 package template.",
    url='https://github.com/astronouth7303/puppies',
    author='Jamie Bliss',
    author_email='james.bliss@astro73.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': []},

    long_description=(README + '\n' + CHANGES),
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
    ],

    install_requires=open('requirements.txt').readlines(),
)
