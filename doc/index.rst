.. Milia documentation master file, created by
   sphinx-quickstart on Tue Feb  7 00:47:28 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyMilia, fast cosmological distances and ages
=============================================

Welcome. This is the Documentation for PyMilia (version |version|, 
date |today|),

PyMilia is provides fast cosmological distances and ages. It is
a wrapper of the C++ library milia. 

Milia computes the common cosmological distances and times.
using elliptical functions instead of integrating numerically the
equations. The luminosity distance is based on [KKT2000]_.
The age is computed using the equations given in [TK2000]_.
The remaining distances are computed using the relations
described in [H1999]_.

The following example shows how PyMilia can be used to compute
cosmological distances and ages:

.. code-block:: python

   >>> from milia import Metric

   # Hubble parameter, matter density
   # and vaccum density
   >>> metric = Metric(73, 0.27, 0.73)
   # Luminosity distance in Mpc
   >>> metric.dl(2.34)
   18568.03817428285

   # Age in Gyr
   >>> metric.age(1)
   5.777105613197691


Documentation:

.. toctree::
   installation
   using
   reference

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. [H1999]  *Distance measures in cosmology*,  `Hogg (1999) <http://xxx.unizar.es/abs/astro-ph/9905116>`_
.. [KKT2000] *Distance-Redshift in Inhomogeneous FLRW*, `Kantowski, Kao & Thomas (2000) <http://xxx.unizar.es/abs/astro-ph/0002334>`_
.. [TK2000] *The Age-Redshift Relation for Standard Cosmology*, `Thomas & Kantowski (2000)  <http://xxx.unizar.es/abs/astro-ph/0003463>`_
