
Obtaining and installing
========================

PyMilia is distributed under GNU GPL, either version 3 of the License, 
or (at your option) any later version. See the file LICENSE.txt 
for details.

Requirements
------------

PyMilia requires the following 
packages installed in order to work properly:

 - `milia`_ the underlying C++ library
 - `Cython`_ creates the wrapping code

Additional packages are optionally required:
 - `sphinx`_  to build the documentation
 - `nose`_  to run the tests

Installing `milia`_
+++++++++++++++++++
PyMilia requires `milia`_ >= 1.0.0. The installation of milia
is detailled elsewhere, but here we show a few steps.

 * Check if milia is available precompilled in your package manager of choice.
   If it is, install the library package **and** the development package.

 * If not, install milia requirements: `GSL`_ and `Boost`_. `Cppunit`_ 
   is required only to run the tests.

 * Download milia tarball.

 * Untar and run `./configure` and `make install`::

    $ tar zxvf milia-X.Y.Z.tar.gz
    $ cd milia-X.Y.Z
    $ ./configure
    # if configure ends without errors
    $ make
    $ make check
    $ make install

By default installation requires administrative privileges. 

Stable version
--------------

The latest stable version of PyMilia can be downloaded from  
ftp://astrax.fis.ucm.es/pub/software/milia

To install PyMilia, use the standard installation procedure:::

    $ tar zxvf pymilia-X.Y.Z.tar.gz
    $ cd pymilia-X.Y.Z
    $ python setup.py install
    
The `install` command provides options to change the target directory. 
By default installation requires administrative privileges. 
The different installation options can be checked with::: 

   $ python setup.py install --help
   
Development version
-------------------

The development version can be checked out with:::

    $ hg clone https://guaix.fis.ucm.es/hg/pymilia

And then installed following the standard procedure:::

    $ cd pymilia
    $ python setup.py install

Building the documentation
---------------------------
The PyMilia documentation is base on `sphinx`_. With the package 
installed, the 
html documentation can be built::

  $ python setup.py build_sphinx
  
The documentation will be copied to a directory under `build/sphinx`.
  
The documentation can be built in different formats. The complete list will appear if you type::

  $ python setup.py build_sphinx --help

.. _milia: http://guaix.fis.ucm.es/projects/milia
.. _sphinx: http://sphinx.pocoo.org
.. _Cython: http://cython.org
.. _nose: http://cython.org
.. _gsl: http://www.gnu.org/software/gsl/
.. _boost: http://www.boost.org
.. _cppunit: http://sourceforge.net/apps/mediawiki/cppunit/index.php?title=Main_Page

