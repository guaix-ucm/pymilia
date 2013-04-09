#
# Copyright 2009-2013 Sergio Pascual
# 
# This file is part of PyMilia
# 
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# PyMilia is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with PyMilia.  If not, see <http://www.gnu.org/licenses/>.
#

'''Pure Python implementation of Flrw and FlrwNat'''

from __future__ import division

import math
from scipy.special import cbrt, ellipkinc

M_SQRT3 = math.sqrt(3)
M_4THRT3 = math.sqrt(M_SQRT3)

def sinc(k, a, x):
    if k == 1:
        return math.sin(a * x) / a
    elif k == -1:
        return math.sinh(a * x) / a
    elif k == 0:
        return x
    return 0

def asinc(k, a, x):
    if k == 1:
        return math.asin(a * x) / a
    elif k == -1:
        return math.asinh(a * x) / a
    elif k == 0:
        return x
    return 0

class Flrw(object):
    '''The Friedmann-Lemaitre-Robertson-Walker metric

    This class represents a FLRW metric. Its methods compute the
    common cosmological distances and times.
    '''
    def __init__(self, hubble, matter, vacuum):
        '''The constructor takes three parameters:

        :param hubble: Hubble parameter in km / s / Mpc
        :param matter: mater density (adimensional)
        :param vacuum: vacuum energy density (adimensional)

        '''
        self.nat = FlrwNat(matter, vacuum)
        self.hubble = hubble
        self.hubble_radius = 299792.458 / self.hubble

    def age(self, z=None):
        '''Return the age of the Universe [Gyr].

        :param z: redshift
        :returns: age of the Universe [Gyr].

        '''
        if z is not None:
            return 0
        else:
            return 0

    def angular_scale(self, z):
        '''Return the factor to transform angular sizes in pc to arc sec.

        :param z: redshift
        :returns: factor to transform angular sizes in pc to arc sec

        '''
        return 0

    def dc(self, z):
        '''Return the comoving distance in the line of sight [Mpc].

        :param z: redshift
        :returns: comoving distance in the line of sight [Mpc]
        
        '''
        return self.hubble_radius * self.nat.dc(z)
        
    def dl(self, z):
        '''Return the luminosity distance [Mpc].

        :param z: redshift
        :returns: luminosity distance [Mpc]

        '''
        return self.hubble_radius * self.nat.dl(z)

    def dm(self, z):
        '''Return the comoving distance in transverse direction [Mpc].

        :param z: redshift
        :returns: comoving distance in transverse direction [Mpc]
        
        '''
        return self.hubble_radius * self.nat.dm(z)

    def da(self, z):
        '''Return the angular distance [Mpc].
        
        :param z: redshift
        :returns: angular distance [Mpc] 
        
        '''
        return self.hubble_radius * self.nat.da(z)

    def lt(self, z):
        '''Return the look-back time [Gyr].
        
        :param z: redshift
        :returns: look-back time [Gyr]
        
        '''
        return 0

    def vol(self, z):
        '''Return comoving volume per solid angle [Mpc^3 sr^-1]
        
        :param z: redshift
        :returns: comoving volume per solid angle [Mpc^3 sr^-1]
        
        '''
        return self.hubble_radius * self.hubble_radius * self.hubble_radius * self.nat.vol(z)

    def __str__(self):
        return 'milia.Flrw(hubble=%f, matter=%f, vacuum=%f)' % (self.hubble, self.matter, self.vacuum)

#    property matter:
#        def __get__(self): return (<flrw_nat *>(self.thisptr)).get_matter()
#        def __set__(self, m): (<flrw_nat *>(self.thisptr)).set_matter(m)

#    property vacuum:
#        def __get__(self): return (<flrw_nat *>(self.thisptr)).get_vacuum()
#        def __set__(self, m): (<flrw_nat *>(self.thisptr)).set_vacuum(m)

#    property hubble:
#        def __get__(self): return self.thisptr.get_hubble()
#        def __set__(self, m): self.thisptr.set_hubble(m)

# END


# Factory function
def FlrwNat(matter, vacuum):

    if matter == 0 and vacuum == 0:
        return Flrw_OM_OV_0()

    if matter == 0 and vacuum == 1:
        return Flrw_OM_DS()
    if matter == 0 and 0 < vacuum < 1:
        return Flrw_OM(vacuum)

    if matter == 1 and vacuum == 0:
        return Flrw_OV_EDS()
    if matter < 1 and vacuum == 0:
        return Flrw_OV_1(matter)
    if matter > 1 and vacuum == 0:
        return Flrw_OV_2(matter)

    if matter + vacuum == 1:
        return Flrw_OM_OV_1(matter)
    
    ok = 1 - matter - vacuum
    crit = -13.5 * matter**2 * vacuum / ok**3

    if crit == 2:
        return FlrwA2_1(matter, vacuum)
    elif 0 < crit < 2:
        return FlrwA2_2(matter, vacuum)
    elif crit > 2 or crit < 0:
        return FlrwA1(matter, vacuum)

    return FlrwNonFlat(matter, vacuum)

class FlrwBaseImpl(object):
    '''The Friedmann-Lemaitre-Robertson-Walker metric

    This class represents a FLRW metric. Its methods compute the
    common cosmological distances and times.
    '''
    def __init__(self, matter, vacuum):
        '''The constructor takes three parameters:

        :param matter: mater density (adimensional)
        :param vacuum: vacuum energy density (adimensional)

        '''
        self.om = matter
        self.ov = vacuum
        self.ok = 1 - matter - vacuum
        self.kap = -1 if self.ok > 0 else 1
        self.sqok = math.sqrt(abs(self.ok))

    @property 
    def matter(self):
        return self.om

    @property 
    def vaccum(self):
        return self.ov

    def age(self, z=None):
        '''Return the age of the Universe [Gyr].

        :param z: redshift
        :returns: age of the Universe [Gyr].

        '''
        if z is not None:
            return 0
        else:
            return 0

    def angular_scale(self, z):
        '''Return the factor to transform angular sizes in pc to arc sec.

        :param z: redshift
        :returns: factor to transform angular sizes in pc to arc sec

        '''
        return 0

    def dc(self, z):
        '''Return the comoving distance in the line of sight [Mpc].

        :param z: redshift
        :returns: comoving distance in the line of sight [Mpc]
        
        '''
        raise NotImplementedError
        
    def dl(self, z):
        '''Return the luminosity distance [Mpc].

        :param z: redshift
        :returns: luminosity distance [Mpc]

        '''
        print self
        raise NotImplementedError

    def dm(self, z):
        '''Return the comoving distance in transverse direction [Mpc].

        :param z: redshift
        :returns: comoving distance in transverse direction [Mpc]
        
        '''
        return self.dl(z) / (1 + z)

    def da(self, z):
        '''Return the angular distance [Mpc].
        
        :param z: redshift
        :returns: angular distance [Mpc] 
        
        '''
        return self.dl(z) / ((1 + z) * (1 + z))

    def lt(self, z):
        '''Return the look-back time [Gyr].
        
        :param z: redshift
        :returns: look-back time [Gyr]
        
        '''
        return 0

    def vol(self, z):
        '''Return comoving volume per solid angle [Mpc^3 sr^-1]
        
        :param z: redshift
        :returns: comoving volume per solid angle [Mpc^3 sr^-1]
        
        '''
        raise NotImplementedError

    def __str__(self):
        return 'milia.Flrw(matter=%f, vacuum=%f)' % (self.om, self.ov)

#    property matter:
#        def __get__(self): return (<flrw_nat *>(self.thisptr)).get_matter()
#        def __set__(self, m): (<flrw_nat *>(self.thisptr)).set_matter(m)

#    property vacuum:
#        def __get__(self): return (<flrw_nat *>(self.thisptr)).get_vacuum()
#        def __set__(self, m): (<flrw_nat *>(self.thisptr)).set_vacuum(m)

#    property hubble:
#        def __get__(self): return self.thisptr.get_hubble()
#        def __set__(self, m): self.thisptr.set_hubble(m)

class FlrwFlat(FlrwBaseImpl):
    def __init__(self, matter, vacuum):
        super(FlrwFlat, self).__init__(matter, vacuum)

    def dc(self, z):
        return self.dm(z)

    def vol(self, z):
        dm = self.dm(z)
        return dm * dm * dm / 3

class Flrw_OV_EDS(FlrwFlat):
    def __init__(self):
        super(Flrw_OV_EDS, self).__init__(1.0, 0.0)

    def dl(self, z):
        return 2 * (1 + z - math.sqrt(1 + z))
    
    def age(self, z):
        return 2 / (3 * (1 + z) * math.sqrt(1 + z))

class Flrw_OM_DS(FlrwFlat):
    def __init__(self):
        super(Flrw_OM_DS, self).__init__(0.0, 1.0)

    def dl(self, z):
        return z * (z + 1)

class Flrw_OM_OV_1(FlrwFlat): # OM_OV_1
    def __init__(self, matter):
        super(Flrw_OM_OV_1, self).__init__(matter, 1 - matter)
        self.k = 0.5 + 0.25 * M_SQRT3
        self.arg0 = cbrt(1 / self.om - 1)
        self.factor = math.sqrt(M_SQRT3 * self.om * self.arg0)
        self.down = 1 + (1 + M_SQRT3) * self.arg0
        self.up = 1 + (1 - M_SQRT3) * self.arg0
        self.phi0 = math.acos(self.up / self.down)

    def dl(self, z):
        phi = math.acos((z + self.up) / (z + self.down))
        return (1 + z) / self.factor * (ellipkinc(self.phi0, self.k) - ellipkinc(phi, self.k))

    def age(self, z):
        return 2. / (3. * math.sqrt(1 - self.om)) * math.asinh(sqrt((1 / self.om - 1) / (1 + z)**3))

class FlrwNonFlat(FlrwBaseImpl):
    def __init__(self, matter, vacuum):
        super(FlrwNonFlat, self).__init__(matter, vacuum)

    def dc(self, z):
        dm = self.dm(z)
        return asinc(self.kap, self.sqok, dm)

    def vol(self, z):
        dm = self.dm(z)
        return (dm * math.sqrt(1 + self.ok * dm * dm) - asinc(self.kap, self.sqok, dm)) / (2 * self.ok)

class Flrw_OM_OV_0(FlrwNonFlat):
    def __init__(self):
        super(Flrw_OM_OV_0, self).__init__(0.0, 0.0)

    def dl(self, z):
        return 0.5 * z * (z + 2)

    def age(self, z):
        return 1 / (1 + z)

class Flrw_OM(FlrwNonFlat):
    def __init__(self, vacuum):
        super(Flrw_OM, self).__init__(0.0, vacuum)

    def dl(self, z):
        return ((1 + z) / self.ov) * (1 + z - math.sqrt(self.ov + (1 - self.ov) * (1 + z)*(1+z)))

class Flrw_OV(FlrwNonFlat):
    def __init__(self, matter):
        super(Flrw_OV, self).__init__(matter, 0.0)

    def dl(self, z):
        return 2 * ((2 - self.om * (1 - z) - (2 - self.om) * math.sqrt(1 + self.om * z))) / (self.om * self.om)

class Flrw_OV_1(Flrw_OV):
    def __init__(self, matter):
        super(Flrw_OV_1, self).__init__(matter)

class Flrw_OV_2(Flrw_OV):
    def __init__(self, matter):
        super(Flrw_OV_2, self).__init__(matter)

class FlrwA(FlrwNonFlat):
    def __init__(self, matter, vacuum):
        super(FlrwA, self).__init__(matter, vacuum)
        self.crit = -13.5 * matter**2 * vacuum / self.ok**3

class FlrwA1(FlrwA):
    def __init__(self, matter, vacuum):
        super(FlrwA1, self).__init__(matter, vacuum)

    def dl(self, z):
        v = cbrt(self.kap * (self.crit - 1) + math.sqrt(self.crit * (self.crit - 2)))
        y = (-1 + self.kap * (v + 1. / v)) / 3
        A = math.sqrt(y * (3 * y + 2))
        g = 1 / math.sqrt(A)
        k = 0.5 + 0.25 * g * g * (v + 1 / v)
        sup = self.om / abs(self.ok)
        phi = math.acos(((1 + z) * sup + self.kap * y - A) / ((1 + z) * sup + self.kap * y + A))
        phi0 = math.acos((sup + self.kap * y - A) / (sup + self.kap * y + A)) 
        return (1 + z) / self.sqok * sinc(self.kap, 1.0, g * (ellipkinc(phi0, k) - ellipkinc(phi, k)))

class FlrwA2(FlrwA):
    def __init__(self, matter, vacuum):
        super(FlrwA2, self).__init__(matter, vacuum)

    def dl(self, z):
        arg0 = math.acos(1 - self.crit) / 3
        arg1 = self.om / abs(self.ok);
        y1 = (-1 + math.cos(arg0) + M_SQRT3 * math.sin(arg0)) / 3
        y2 = (-1 - 2 * math.cos(arg0)) / 3
        y3 = (-1 + math.cos(arg0) - M_SQRT3 * math.sin(arg0)) / 3
        g = 2 / math.sqrt(y1 - y2)
        k = (y1 - y3) / (y1 - y2)
        phi = math.asin(math.sqrt((y1 - y2) / ((1 + z) * arg1 + y1)))
        phi0 = math.asin(math.sqrt((y1 - y2) / (arg1 + y1)))
        return (1. + z) / self.sqok * math.sin(g * (ellipkinc(phi0, k) - ellipkinc(phi, k)))

class FlrwA2_1(FlrwA2):
    def __init__(self, matter, vacuum):
        super(FlrwA2_1, self).__init__(matter, vacuum)

class FlrwA2_2(FlrwA2):
    def __init__(self, matter, vacuum):
        super(FlrwA2_2, self).__init__(matter, vacuum)

if __name__ == '__main__':

    a = Flrw(70, 0.3, 0.6)
    print a.dc(1)
