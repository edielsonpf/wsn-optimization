
#! /usr/bin/env python
#
# Copyright (C) 2020 wsn-toolkit
#
# This program was written by Edielson P. Frigieri <edielsonpf@gmail.com>
#               
# License: MIT

from setuptools import setup, find_packages

setup(
    name='wsn-toolkit', 
    version='0.0.1',
    description='A toolkit for Wireless Sensor Networks',
    long_description='wsn-toolkit is a Python module for simulation of Wireless Sensor Networks',
    url='https://github.com/edielsonpf/wsn-toolkit', 
    author='Edielson P. Frigieri',  
    author_email='edielsonpf@gmail.com',
    license="MIT",
    classifiers=[  
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
    install_requires=[
       "pytest",
       "numpy",
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    keywords='wsn, tools, sensor',
    packages=find_packages(include=['wsntk', 'wsntk.*']),
    python_requires='>=3.5, <4',
    project_urls={ 'Source': 'https://github.com/edielsonpf/wsn-toolkit',},
)