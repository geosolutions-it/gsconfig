#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    readme_text = open('README.rst', 'r').read()
except IOError:
    readme_text = ''

setup(
    name="gsconfig",
    version="2.0.1",
    description="GeoServer REST Configuration",
    long_description=readme_text,
    keywords="GeoServer REST Configuration",
    license="MIT",
    url="https://github.com/boundlessgeo/gsconfig",
    author="David Winslow, Sebastian Benthall",
    author_email="dwinslow@opengeo.org",
    install_requires=[
        'requests >= 2.14.0',
        'gisdata == 0.5.4',
        'future'
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    test_suite="test.catalogtests",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
