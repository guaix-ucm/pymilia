#!/usr/bin/env python

from distutils.core import setup, Extension

ext1 = Extension('milia.metrics', ['src/metrics_wrap.cc'], 
  libraries = ['boost_python', 'milia', 'gsl', 'gslcblas'])
ext2 = Extension('milia.lumfuncs', ['src/lumfuncs_wrap.cc'], 
  libraries = ['boost_python', 'milia', 'gsl', 'gslcblas'])

setup(name='pymilia',
      version='0.2.0',
      author='Sergio Pascual',
      author_email='spr@astrax.fis.ucm.es',
      url='https:// halmax.fis.ucm.es/projects/milia/wiki',
      license='GPLv3',
      description='Cosmological distances and ages',
      package_dir={'milia': 'lib/milia'},
      packages=['milia'],
      ext_modules=[ext1, ext2],
      )
