#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import pathlib
import os
import platform
import sys
import warnings


REQUIRED = [
    'requests',
    'numpy',
    'pandas',
    'geopandas',
    'shapely',
    'fiona',
]

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
  author="Marc Rauckhorst",
  author_email='mwrauck@sas.upenn.edu',
  url="https://github.com/marc-rauckhorst/arcos-py",
  classifiers=[
    'License :: OSI Approved :: MIT License',
    #'Programming Language :: Python :: 3.5'
    #'Programming Language :: Python :: 3.6'
    'Programming Language :: Python :: 3.7',
  ],
  description="Python package to directly access the Washington Post's ARCOS API and opioid dataset",
  license="MIT license",
  include_package_data=True,
  packages=find_packages(exclude=("tests",)),
  install_requires = REQUIRED,
  name='arcos4py',
  version='0.2.2',
  zip_safe=False,
)

