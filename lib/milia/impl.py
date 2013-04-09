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

