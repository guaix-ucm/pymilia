
cdef extern from "milia/flrw_nat.h" namespace "milia":
    cdef cppclass flrw_nat:
        flrw_nat(double, double) except+
        double dc(double)
        double dm(double)
        double da(double)
        double dl(double)
        double lt(double)
        double vol(double)
        double age()
        double age(double)
        double get_matter()
        double set_matter(double)
        double get_vacuum()
        double set_vacuum(double)

cdef extern from "milia/flrw.h" namespace "milia":
    cdef cppclass flrw:
        flrw(double, double, double) except+
        double dc(double)
        double dm(double)
        double da(double)
        double dl(double)
        double lt(double)
        double vol(double)
        double age()
        double age(double)
        double angular_scale(double)
#        double hubble_radius()
#        double hubble_time()
        double get_hubble()
        double set_hubble(double)

cdef class FlrwNat:
    '''The Friedmann-Lemaitre-Robertson-Walker metric in natural units.

    This class represents a FLRW metric in natural units. Its methods 
    compute the common cosmological distances and times.

    '''
    cdef flrw_nat *thisptr
    def __cinit__(self, double matter, double vacuum):
        '''The constructor takes two parameters:

        :param matter: mater density [adimensional]
        :param vacuum: vacuum energy density [adimensional]

        '''
        self.thisptr = new flrw_nat(matter, vacuum)

    def __dealloc__(self):
        del self.thisptr

    def age(self, z):
        '''Return the age of the Universe [adimensional].

        :param z: redshift
        :returns: age of the Universe [adimensional].

        '''
        return self.thisptr.age(z)

    def dc(self, z):
        '''Return the comoving distance in the line of sight [adimensional].

        :param z: redshift
        :returns: comoving distance in the line of sight [adimensional]
        
        '''
        return self.thisptr.dc(z)
        
    def dl(self, z):
        '''Return the luminosity distance [adimensional].

        :param z: redshift
        :returns: luminosity distance [adimensional]

        '''
        return self.thisptr.dl(z)

    def dm(self, z):
        '''Return the comoving distance in transverse direction [adimensional].

        :param z: redshift
        :returns: comoving distance in transverse direction [adimensional]
        
        '''
        return self.thisptr.dm(z)

    def da(self, z):
        '''Return the angular distance [adimensional].
        
        :param z: redshift
        :returns: angular distance [adimensional]
        
        '''
        return self.thisptr.da(z)

    def lt(self, z):
        '''Return the look-back time [adimensional].
        
        :param z: redshift
        :returns: look-back time in [adimensional]
        
        '''
        return self.thisptr.lt(z)

    def vol(self, z):
        '''Return comoving volume per solid angle [adimensional].
        
        :param z: redshift
        :returns: comoving volume per solid angle [adimensional]
        
        '''
        return self.thisptr.vol(z)

    property matter:
        def __get__(self): return self.thisptr.get_matter()
        def __set__(self, m): self.thisptr.set_matter(m)

    property vacuum:
        def __get__(self): return self.thisptr.get_vacuum()
        def __set__(self, m): self.thisptr.set_vacuum(m)

    def __str__(self):
        return 'milia.FlrwNat(matter=%f, vacuum=%f)' % (self.matter, self.vacuum)

cdef class Flrw:
    '''The Friedmann-Lemaitre-Robertson-Walker metric

    This class represents a FLRW metric. Its methods compute the
    common cosmological distances and times.
    '''
    cdef flrw *thisptr
    def __cinit__(self, double hubble, double matter, double vacuum):
        '''The constructor takes three parameters:

        :param hubble: Hubble parameter in km / s / Mpc
        :param matter: mater density (adimensional)
        :param vacuum: vacuum energy density (adimensional)

        '''

        self.thisptr = new flrw(hubble, matter, vacuum)

    def __dealloc__(self):
        del self.thisptr

    def age(self, z):
        '''Return the age of the Universe [Gyr].

        :param z: redshift
        :returns: age of the Universe [Gyr].

        '''
        return self.thisptr.age(z)

    def angular_scale(self, z):
        '''Return the factor to transform angular sizes in pc to arc sec.

        :param z: redshift
        :returns: factor to transform angular sizes in pc to arc sec

        '''
        return self.thisptr.angular_scale(z)

    def dc(self, z):
        '''Return the comoving distance in the line of sight [Mpc].

        :param z: redshift
        :returns: comoving distance in the line of sight [Mpc]
        
        '''
        return self.thisptr.dc(z)
        
    def dl(self, z):
        '''Return the luminosity distance [Mpc].

        :param z: redshift
        :returns: luminosity distance [Mpc]

        '''
        return self.thisptr.dl(z)

    def dm(self, z):
        '''Return the comoving distance in transverse direction [Mpc].

        :param z: redshift
        :returns: comoving distance in transverse direction [Mpc]
        
        '''
        return self.thisptr.dm(z)

    def da(self, z):
        '''Return the angular distance [Mpc].
        
        :param z: redshift
        :returns: angular distance [Mpc] 
        
        '''
        return self.thisptr.da(z)

    def lt(self, z):
        '''Return the look-back time [Gyr].
        
        :param z: redshift
        :returns: look-back time [Gyr]
        
        '''
        return self.thisptr.lt(z)

    def vol(self, z):
        '''Return comoving volume per solid angle [Mpc^3 sr^-1]
        
        :param z: redshift
        :returns: comoving volume per solid angle [Mpc^3 sr^-1]
        
        '''
        return self.thisptr.vol(z)

    def __str__(self):
        return 'milia.Flrw(hubble=%f, matter=%f, vacuum=%f)' % (self.hubble, self.matter, self.vacuum)

    property matter:
        def __get__(self): return (<flrw_nat *>(self.thisptr)).get_matter()
        def __set__(self, m): (<flrw_nat *>(self.thisptr)).set_matter(m)

    property vacuum:
        def __get__(self): return (<flrw_nat *>(self.thisptr)).get_vacuum()
        def __set__(self, m): (<flrw_nat *>(self.thisptr)).set_vacuum(m)

    property hubble:
        def __get__(self): return self.thisptr.get_hubble()
        def __set__(self, m): self.thisptr.set_hubble(m)
