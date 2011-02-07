.. PyMilia documentation master file, created by
   sphinx-quickstart on Sat Feb  5 18:07:35 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyMilia
=======

============
Installation
============

Blah, blah, blah,

=================
API Documentation
=================

.. class:: Flrw(hubble, matter, vacuum)

   The Friedmann-Lemaitre-Robertson-Walker metric

   This class represents a FLRW metric. Its methods compute the
   common cosmological distances and times.
   It is based on the `Hogg 1999 <http://xxx.unizar.es/abs/astro-ph/9905116>`_ for the relations between distances.
   The age and distance luminosity are computed from `Thomas & Kantowski 2000
   <http://xxx.unizar.es/abs/astro-ph/0003463>`_ with elliptical functions.
   Distances are computed from the luminosity distance using 
   `Kantowski, Kao & Thomas <http://xxx.unizar.es/abs/astro-ph/0002334>`_
   without inhomogeneities.

   .. method:: age(z)

      Age of the Universe in Gyr

      :param z: redshift
      :return: age of the Universe in Gyr

   .. method:: dm(z)

      Comoving distance (transverse) in Mpc

      :param z: redshift
      :return: transverse comoving distance in Mpc

   .. method:: dc(z)

      Comoving distance (line of sight) in Mpc

      .. math::
         D_c(z)=\frac{c}{H_0}\int_0^z \frac{dt}{\sqrt{\Omega_m(1+t)^3+\Omega_k(1+t)^2+\Omega_v}}

      :param z: redshift
      :return: line of sight comoving distance in Mpc

   .. method:: dl(z)

      Luminosity distance in Mpc

      :param z: redshift
      :return: the luminosity distance in Mpc

   .. method:: da(z)

      Angular distance in Mpc

      .. math::
         D_a(z) = \frac{1}{1 + z} D_m(z)

      :param z: redshift
      :return: angular distance in Mpc

   .. method:: lt(z)

      Look-back time in Gyr

      :param z: redshift
      :return: look-back time in Gyr

   .. method:: vol(z)

      Comoving volume per solid angle

      :param z: redshift
      :return: comoving volume in Mpc^3 per solid angle


   .. attribute:: hubble

      Hubble parameter

   .. attribute:: matter

      Value of the vacuum energy density :math:`\Omega_m`.

   .. attribute:: vacuum

      Value of the vacuum energy density :math:`\Omega_v`.


Contents:

.. toctree::
   :maxdepth: 2


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

