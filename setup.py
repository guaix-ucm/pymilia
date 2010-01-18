#!/usr/bin/env python

from setuptools import setup, Extension

ext1 = Extension('milia.metrics', ['src/metrics_wrap.cc'],
  libraries=['boost_python', 'milia', 'gsl', 'gslcblas'])
ext2 = Extension('milia.lumfuncs', ['src/lumfuncs_wrap.cc'],
  libraries=['boost_python', 'milia', 'gsl', 'gslcblas'])

setup(name='pymilia',
      version='0.3.0',
      author='Sergio Pascual',
      author_email='sergiopr@astrax.fis.ucm.es',
      url='https://guaix.fis.ucm.es/projects/milia/wiki',
      download_url='ftp://astrax.fis.ucm.es/pub/users/spr/milia/pymilia-0.3.0.tar.gz',
      license='GPLv3',
      description='Cosmological distances and ages',
      package_dir={'milia': 'lib/milia'},
      packages=['milia'],
      ext_modules=[ext1, ext2],
      classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Astronomy",
        ],
      long_description='''\
          This is PyMilia, a set of Python bindings for milia.
        
         Milia is library that provides distances and ages in cosmology.

         Pymilia requires a functional milia installation, and 
         boost (http://www.boost.org/), a C++ library that provides 
         the wrapping library.

         This package is distributed under GPL , either version 3 of the License, or
         (at your option) any later version. See the file COPYING for details.

         ''',
      )
