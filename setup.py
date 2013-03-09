#!/usr/bin/env python

from distutils.core import setup

requirements = [
    'doctest',
    'argparse',
]

setup(
    name='doctestall',
    version='1.0.0',
    description='Recursive tester for doctest-y projects',
    long_description=open('README.md').read(),
    url='https://github.com/campadrenalin/DoctestAll',
    author='Philip Horger',
    author_email='philip.horger@gmail.com',
    install_requires = requirements,
    requires = requirements,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Documentation',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
    py_modules=[
        'doctestall',
    ],
    scripts=[
        'doctestall',
    ],
)
