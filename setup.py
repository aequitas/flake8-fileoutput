# coding: utf-8

from __future__ import with_statement
from setuptools import setup


def get_version(fname='flake8_fileoutput.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in ('README.rst', ):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


setup(
    name='flake8-fileoutput',
    version=get_version(),
    description="File output plugin for flake8",  # noqa
    long_description=get_long_description(),
    keywords='flake8 fileoutput',
    author='Johan Bloemberg',
    author_email='johan.bloemberg@spilgames.com',
    url='https://github.com/spil-johan/flake8-fileoutput',
    license='',
    py_modules=['flake8_fileoutput'],
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'flake8_fileoutput = flake8_fileoutput:FileOutput',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
