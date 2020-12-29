
#! /usr/bin/env python
#
# Copyright (C) 2020 wsn-toolkit
#
# This program was written by Edielson P. Frigieri <edielsonpf@gmail.com>
#               
# License: MIT

from setuptools import setup, find_packages

setup(

    setup_requires=['pytest-runner', 'pbr'],
    pbr=True,
    tests_require=['pytest'],
)