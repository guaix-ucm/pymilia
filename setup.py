#!/usr/bin/env python

from setuptools import setup, Extension
from Cython.Distutils import build_ext

ext1=Extension('milia._milia', ['src/milia.pyx'],
               language="c++",
               libraries=['milia'])

setup(name='pymilia',
      version='1.1.0dev',
      author='Sergio Pascual',
      author_email='sergiopr@fis.ucm.es',
      url='https://guaix.fis.ucm.es/projects/pymilia/wiki',
      download_url='ftp://astrax.fis.ucm.es/pub/software/pymilia-1.0.0.tar.gz',
      license='GPLv3',
      description='Cosmological distances and ages',
      package_dir={'milia': 'lib/milia'},
      packages=['milia', 'milia.tests'],
      requires=['cython'],
      install_requires=['cython'],
      ext_modules=[ext1],
      test_suite="nose.collector",
      tests_require=['nose'],
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
      long_description=open('README.txt').read(),
      )
