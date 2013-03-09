#!/usr/bin/env python

from distutils.core import setup

long_description = '''
DoctestAll
==========

Recursive doctest-executing library and script for running doctest on projects.

DoctestAll is a very simple solution for running unit tests a package at a time,
recursively descending with the ``__all__`` module property to find children
to analyze. Or audit, if you want a creepy scientology metaphor.

DTA is available as the ``doctestall`` module, and a script by the same name
which can be run from the command line.


Installation
============

DTA can be installed via pip:

    sudo pip install doctestall

Or by entering the following commands as administrator:

    git clone git://github.com/campadrenalin/DoctestAll.git

    cd DoctestAll

    python setup.py install

Once installed, you can import the doctestall module, or try it out in the shell:

    doctestall doctestall

Yes, this runs doctestall *on itself.* But to test some other module:

    doctestall cmath

The cmath module doesn't use doctest, so the results are uninteresting, but on
the other hand, the recursive walk doesn't make anything explode either. So you
might want to try it out on projects that are actually designed to use DTA, or
at least be friendly to it.


Projects using or compatible with DTA:
======================================

* `ConcurrenTree <https://github.com/campadrenalin/ConcurrenTree>`_
* `DoctestAll <https://github.com/campadrenalin/DoctestAll>`_
* `EJTP <https://github.com/campadrenalin/EJTP-lib-python>`_
'''

requirements = [
    #'doctest',
    'argparse',
]

setup(
    name='doctestall',
    version='1.0.4',
    description='Recursive tester for doctest-y projects',
    long_description=long_description,
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
