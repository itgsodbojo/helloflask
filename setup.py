#!/usr/bin/env python
import os
from setuptools import setup

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

exec(open('helloflask/version.py').read())

with open('./requirements.txt') as reqs_txt:
    requirements = [line for line in reqs_txt]


setup(
    name="helloflask",
    version=version,
    description="helloflask testing deployment",
    packages=['helloflask'],
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    test_suite='tests',
    classifiers=[
        'Development Status :: Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Education :: Testing',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
