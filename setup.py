#!/usr/bin/env python

from distutils.core import setup, Extension

setup(name='pymilia',
      version='0.1.0',
      author='Sergio Pascual',
      author_email='spr@astrax.fis.ucm.es',
      url='http://guaix.fis.ucm.es',
      ext_modules=[Extension('milia',
                             ['milia_wrap.cc'],
                             libraries=['boost_python','milia',
                                        'gsl','gslcblas'])
      ],
      )
