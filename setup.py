#!/usr/bin/env python

from setuptools import setup, Extension

import commands

## {{{ http://code.activestate.com/recipes/502261/ (r1)
def pkgconfig(*packages, **kw):
    flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
    for token in commands.getoutput("pkg-config --libs --cflags %s" % ' '.join(packages)).split():
        kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
    return kw

kw = pkgconfig('milia', 'gsl', libraries=['boost_python'])


ext1 = Extension('milia', ['src/metrics_wrap.cc'], **kw)

setup(name='pymilia',
      version='0.4.0alpha',
      author='Sergio Pascual',
      author_email='sergiopr@fis.ucm.es',
      url='https://guaix.fis.ucm.es/projects/pymilia/wiki',
      download_url='ftp://astrax.fis.ucm.es/pub/users/spr/milia/pymilia-0.4.0.tar.gz',
      license='GPLv3',
      description='Cosmological distances and ages',
      package_dir={'milia': 'lib/milia'},
      packages=['milia', 'milia.tests'],
      ext_modules=[ext1],
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
