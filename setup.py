#!/usr/bin/env python
import sys
import os.path

from setuptools import setup, find_packages, Extension

try:
    from Cython.Build import cythonize
except ImportError:
    extensions = [
        Extension(
            'simdjson.csimdjson',
            sources=[
                'simdjson/csimdjson.cpp'
            ],
            language='c++'
        )
    ]
else:
    extensions = cythonize([
        Extension(
            'simdjson.csimdjson',
            sources=[
                'simdjson/csimdjson.pyx'
            ],
            language='c++'
        )
    ], compiler_directives={
        # Make sure we embed function signatures as the first line of the
        # docstring so sphinx can pull them out for documentation.
        'embedsignature': True
    })

root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), 'rb') as readme:
    long_description = readme.read().decode('utf-8')


setup(
    name='pysimdjson',
    packages=find_packages(),
    version='1.3.0',
    description='simdjson bindings for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Tyler Kennedy',
    author_email='tk@tkte.ch',
    url='http://github.com/TkTech/pysimdjson',
    keywords=['json', 'simdjson'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
    ],
    tests_require=[
        'pytest>=2.10',
        'Cython',
        'm2r',
        'sphinx',
        'ghp-import',
        'bumpversion'
    ],
    ext_modules=extensions,
    package_data = {
        'simdjson': ['simdjson/*.pyd']
    }
)
