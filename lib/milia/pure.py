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

class FlrwNat(object):
    '''The Friedmann-Lemaitre-Robertson-Walker metric in natural units.

    This class represents a FLRW metric in natural units. Its methods 
    compute the common cosmological distances and times.

    '''
    def __init__(self, matter, vacuum):
        '''The constructor takes two parameters:

        :param matter: mater density [adimensional]
        :param vacuum: vacuum energy density [adimensional]

        '''
        self.om = matter
        self.ov = vacuum
        self.ok = 1 - matter - vacuum
        self.kap = -1 if self.ok > 0 else 1
        self.sqok = math.sqrt(abs(self.ok))

        if self.ok != 0:
            self.crit = -13.5 * self.om**2 * self.ov / self.ok**3;
        else:
            self.crit = None

        class _CC(object):
            NO_CASE = -1 # error condition
            OM_OV_0 = 0 # om = ov = 0
            OV_1 = 1 # ov = 0 0 < om < 1
            OV_2 = 2 # ov = 0 om > 1
            OV_EDS = 3 # ov = 0 om = 1, Einstein-de Sitter Universe
            OM = 4 # om = 0 0 < ov < 1
            OM_DS = 5 # om = 0 ov = 1, de Sitter Universe
            OM_OV_1 = 6# om + ol = 1
            A1 = 7 # om+ov != 1 b < 0 || b > 2
            A2_1 = 8 # om+ov != 1 b = 2
            A2_2 = 9# om+ov != 1 0 < b < 2

            @classmethod
            def select(cls, matter, vacuum):
                ok = 1 - matter - vacuum 
                if ok != 0:
                    crit = -13.5 * matter**2 * vacuum / ok**3;
                else:
                    crit = None

                l3 = (matter == 0)
                l4 = (vacuum == 0)

                if l3 and l4:
                    return cls.OM_OV_0

                if l4:
                    if matter == 1:
                        return cls.OV_EDS
                    elif matter < 1:
                        return cls.OV_1
                    else:
                        return cls.OV_2

                if l3:
                    if vacuum == 1:
                        return cls.OM_DS
                    if 0 < vacuum < 1:
                        return cls.OM
                if ok == 0:
                    return cls.OM_OV_1

                if crit == 2:
                    return cls.A2_1
                elif 0 < crit < 2:
                    return cls.A2_2
                else:
                    return cls.A1

                return cls.NO_CASE

        self.CC = _CC()
        self.case = _CC.select(self.om, self.ov)

    def age(self, z=None):
        '''Return the age of the Universe [adimensional].

        :param z: redshift
        :returns: age of the Universe [adimensional].

        '''
        return 0

    def dc(self, z):
        '''Return the comoving distance in the line of sight [adimensional].

        :param z: redshift
        :returns: comoving distance in the line of sight [adimensional]
        
        '''
        return self._dc_from_dm(z, self.dm(z))
        
    def dl(self, z):
        '''Return the luminosity distance [adimensional].

        :param z: redshift
        :returns: luminosity distance [adimensional]

        '''
        if self.case == self.CC.OM_OV_0:
            return 0.5 * z * (z + 2)
        elif self.case in (self.CC.OV_1, self.CC.OV_2, self.CC.OV_EDS):
            return 2 * ((2 - self.om * (1 - z) - (2 - self.om) * math.sqrt(1 
                + self.om * z))) / (self.om * self.om)
        elif self.case == self.CC.OM:
            return ((1 + z) / self.ov) * (1 + z - math.sqrt(self.ov 
                + (1 - self.ov) * (1 + z)*(1+z)))
        elif self.case == self.CC.OM_DS:
            return z * (z + 1)
        elif self.case == self.CC.OM_OV_1:
            k = 0.5 + 0.25 * M_SQRT3
            arg0 = cbrt(1 / self.om - 1)
            down = 1 + (1 + M_SQRT3) * arg0
            up = 1 + (1 - M_SQRT3) * arg0
            phi = math.acos((z + up) / (z + down))
            phi0 = math.acos(up / down)
            return (1 + z) / math.sqrt(M_SQRT3 * self.om * arg0) * (ellipkinc(phi0, k) - ellipkinc(phi, k))

        elif self.case == self.CC.A1:
            v = cbrt(self.kap * (self.crit - 1) + math.sqrt(self.crit * (self.crit - 2)))
            y = (-1 + self.kap * (v + 1. / v)) / 3
            A = math.sqrt(y * (3 * y + 2))
            g = 1 / math.sqrt(A)
            k = 0.5 + 0.25 * g * g * (v + 1 / v)
            sup = self.om / abs(self.ok)
            phi = math.acos(((1 + z) * sup + self.kap * y - A) / ((1 + z) * sup + self.kap * y + A))
            phi0 = math.acos((sup + self.kap * y - A) / (sup + self.kap * y + A)) 
            return (1 + z) / self.sqok * sinc(self.kap, 1.0, g * (ellipkinc(phi0, k) - ellipkinc(phi, k)))
        elif self.case in (self.CC.A2_1, self.CC.A2_2):
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
        return 0

    def dm(self, z):
        '''Return the comoving distance in transverse direction [adimensional].

        :param z: redshift
        :returns: comoving distance in transverse direction [adimensional]
        
        '''
        return self._dm_from_dl(z, self.dl(z))

    def da(self, z):
        '''Return the angular distance [adimensional].
        
        :param z: redshift
        :returns: angular distance [adimensional]
        
        '''
        return self._da_from_dl(z, self.dl(z))

    def lt(self, z):
        '''Return the look-back time [adimensional].
        
        :param z: redshift
        :returns: look-back time in [adimensional]
        
        '''
        return 0

    def vol(self, z):
        '''Return comoving volume per solid angle [adimensional].
        
        :param z: redshift
        :returns: comoving volume per solid angle [adimensional]
        
        '''
        return self._vol_from_dm(z, self._dm_from_dl(z, self.dl(z)))

#    property matter:
#        def __get__(self): return self.thisptr.get_matter()
#        def __set__(self, m): self.thisptr.set_matter(m)

#    property vacuum:
#        def __get__(self): return self.thisptr.get_vacuum()
#        def __set__(self, m): self.thisptr.set_vacuum(m)

    def __str__(self):
        return 'milia.FlrwNat(matter=%f, vacuum=%f)' % (self.matter, self.vacuum)

    def _da_from_dl(self, z, dl):
        return self._dm_from_dl(z, dl) / (1 + z)

    def _dc_from_dm(self, z, dm):
        if self.case in (self.CC.OM_DS, self.CC.OM_OV_1, self.CC.OV_EDS):
            return dm
        return asinc(self.kap, self.sqok, dm)

    def _dm_from_dl(self, z, dl):
        return dl / (1 + z)

    def _vol_from_dm(self, z, dm):
        if self.case in (self.CC.OM_DS, self.CC.OM_OV_1, self.CC.OV_EDS):
            return dm * dm * dm / 3
        return (dm * math.sqrt(1 + self.ok * dm * dm) - asinc(self.kap, self.sqok, dm)) / (2 * self.ok)

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

if __name__ == '__main__':

    a = FlrwNat(0.3, 0.7)
    print a.dl(1)
    print 1.5428541328556231
    print a.dm(1)
    print 0.7714270664278116
