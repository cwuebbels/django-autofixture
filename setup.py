#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


long_description = u'\n\n'.join((
    open('README.rst').read(),
    open('CHANGES.rst').read(),
))


setup(
    name = 'django-autofixture',
    version = get_version('autofixture'),
    url = 'https://github.com/cwuebbels/django-autofixture',
    license = 'BSD',
    description = 'Provides tools to auto generate test data.',
    long_description = long_description,
    author = 'Gregor Müllegger',
    author_email = 'gregor@muellegger.de',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages = [
        'autofixture',
        'autofixture.management',
        'autofixture.management.commands'],
    install_requires = ['setuptools', 'six'],
    test_suite = 'runtests.runtests',
)
