
#! /usr/bin/env python
#
# Copyright (C) 2020 Edielson P. Frigieri <edielsonpf@gmail.com>
#               
# License: MIT

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
#import pathlib

#here = pathlib.Path(__file__).parent.resolve()
#long_description = (here / 'README.md').read_text(encoding='utf-8')
long_description = "wsn-toolkit is a Python module for simulation of Wireless Sensor Networks"

setup(
    name='wsn-toolkit', 
    version='0.0.1',
    description='A toolkit for Wireless Sensor Networks',
    long_description=long_description,
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
       "Django >= 1.1.1",
       "pytest",
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    keywords='wsn, tools, sensor',
    packages=find_packages(include=['wsntk', 'wsntk.*']),
    python_requires='>=3.5, <4',
    project_urls={ 'Source': 'https://github.com/edielsonpf/wsn-toolkit',},
)