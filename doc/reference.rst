
:mod:`numina` reference
=======================

.. py:module:: numina
   :synopsis: Metric classes

.. py:class:: FlrwNat(matter, vacuum)

    The Friedmann-Lemaitre-Robertson-Walker metric in natural units.

    This class represents a FLRW metric in natural units. Its methods 
    compute the common cosmological distances and times.

    
    :param matter: mater density [adimensional]
    :param vacuum: vacuum energy density [adimensional]


    .. method:: age(z)

        Return the age of the Universe [adimensional].

        :param z: redshift
        :returns: age of the Universe [adimensional].

    .. method:: dc(z)
        Return the comoving distance in the line of sight [adimensional]

        :param z: redshift
        :returns: comoving distance in the line of sight [adimensional]
        
    .. method:: dl(z)
        Return the luminosity distance [adimensional]

        :param z: redshift
        :returns: luminosity distance [adimensional]

    .. method dm(z)
        Return the comoving distance in transverse direction [adimensional].

        :param z: redshift
        :returns: comoving distance in transverse direction [adimensional]
        
    .. method:: da(z)
        Return the angular distance [adimensional].
        
        :param z: redshift
        :returns: angular distance [adimensional]
        
    .. method:: lt(z)
        Return the look-back time [adimensional].
        
        :param z: redshift
        :returns: look-back time in [adimensional]
        
    .. method:: vol(z)
        '''Return comoving volume per solid angle [adimensional].
        
        :param z: redshift
        :returns: comoving volume per solid angle [adimensional]

    .. py:attribute:: matter

        Matter density

    .. py:attribute:: vacuum

.. py:class:: Flrw(hubble, matter, vacuum)

    The Friedmann-Lemaitre-Robertson-Walker metric

    This class represents a FLRW metric. Its methods compute the
    common cosmological distances and times.

    No Big Bang: :math:`\Omega_v > 4 \Omega_m [f(\frac{1}{3}f^{-1}(\Omega_m^{-1} - 1))]^3`
    where :math:`f = \cos` if :math:`\Omega_m > 0.5` and :math:`f = \cosh` if :math:`\Omega_m < 0.5`
         
    Recollapse: 

     * :math:`\Omega_v < 0` 
     * :math:`\Omega_v > 0, \Omega_m > 1` and * :math:`\Omega_v < 4 \Omega_m (\cos(\frac{1}{3}\cos^{-1}(\Omega_m^{-1} - 1) + \frac{4\pi}{3}))^3`
         
    From Cosmological Physics, Peacock pags 82-83


    :param hubble: Hubble parameter in km / s / Mpc
    :param matter: mater density (adimensional)
    :param vacuum: vacuum energy density (adimensional)
    :raise milia.recollapse:
    :throws milia.no_big_bang:


    .. method:: age(z)
        Return the age of the Universe [Gyr].

        :param z: redshift
        :returns: age of the Universe [Gyr].

    .. method:: angular_scale(z)
        Return the factor to transform angular sizes in pc to arc sec.

        :param z: redshift
        :returns: factor to transform angular sizes in pc to arc sec

    .. method:: dc(z)
        Return the comoving distance in the line of sight [Mpc].

        .. math::

              D_c(z)=\frac{c}{H_0}\int_0^z \frac{dt}{\sqrt{\Omega_m(1+t)^3+\Omega_k(1+t)^2+\Omega_v}}

        :param z: redshift
        :returns: comoving distance in the line of sight [Mpc]
        
    .. method:: dl(z)
        Return the luminosity distance [Mpc].

        :param z: redshift
        :returns: luminosity distance [Mpc]

    .. method:: dm(z)
        Return the comoving distance in transverse direction [Mpc].

        :param z: redshift
        :returns: comoving distance in transverse direction [Mpc]
        
    .. method:: da(z)
        Return the angular distance [Mpc].

        .. math:: 

          D_a(z) = \frac{1}{1 + z} D_m(z)
        
        :param z: redshift
        :returns: angular distance [Mpc] 
        
    .. method:: lt(z)
        Return the look-back time [Gyr].
        
        :param z: redshift
        :returns: look-back time [Gyr]
        
    .. method:: vol(z)
        Return comoving volume per solid angle [Mpc^3 sr^-1]
        
        :param z: redshift
        :returns: comoving volume per solid angle [Mpc^3 sr^-1]
        
    .. method:: hubble_radius()
        Return the Hubble radius [Mpc].
        
        :returns: Hubble radius [Mpc]
        
    .. method:: hubble_time()
        Return the Hubble time [Gyr].
        
        :returns: Hubble time [Gyr]
        
    .. py:attribute:: matter

        Matter density

    .. py:attribute:: vacuum
    .. py:attribute:: hubble
