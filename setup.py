#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext1=Extension('milia._milia', ['src/milia.pyx'],
               language="c++",
               libraries=['milia'])


setup(name='pymilia',
      version='1.0.0dev',
      author='Sergio Pascual',
      author_email='sergiopr@astrax.fis.ucm.es',
      url='https://guaix.fis.ucm.es/projects/milia/wiki',
      download_url='ftp://astrax.fis.ucm.es/pub/users/spr/milia/pymilia-1.0.0dev.tar.gz',
      license='GPLv3',
      description='Cosmological distances and ages',
      package_dir={'milia': 'lib/milia'},
      packages=['milia', 'milia.tests'],
      ext_modules=[ext1],
      cmdclass={'build_ext': build_ext},
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
         Cython (http://cython.org/) for building the wrapper. 

         This package is distributed under GPL , either version 3 of the License, or
         (at your option) any later version. See the file COPYING for details.

         ''',
      )
