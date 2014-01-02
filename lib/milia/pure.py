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

'''Pure Python implementation of Flrw'''

from __future__ import division

import math

from factory import FlrwNat

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
        self.hubble_time =  977.792222 / self.hubble

    def age(self, z=None):
        '''Return the age of the Universe [Gyr].

        :param z: redshift
        :returns: age of the Universe [Gyr].

        '''
        return self.hubble_time * self.nat.age(z)

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
        return 'milia.Flrw(hubble=%f, matter=%f, vacuum=%f)' % (self.hubble, self.nat.om, self.nat.ov)

#    property matter:
#        def __get__(self): return (<flrw_nat *>(self.thisptr)).get_matter()
#        def __set__(self, m): (<flrw_nat *>(self.thisptr)).set_matter(m)

#    property vacuum:
#        def __get__(self): return (<flrw_nat *>(self.thisptr)).get_vacuum()
#        def __set__(self, m): (<flrw_nat *>(self.thisptr)).set_vacuum(m)

#    property hubble:
#        def __get__(self): return self.thisptr.get_hubble()
#        def __set__(self, m): self.thisptr.set_hubble(m)

