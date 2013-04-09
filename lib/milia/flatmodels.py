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

from impl import FlrwBaseImpl

M_SQRT3 = math.sqrt(3)

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

    # Age is not defined in this model (since there is no BB)
    # But lookback time is
    def lt(self, z):
        return math.log(1 + z)

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
        return 2. / (3. * math.sqrt(self.ov)) * math.asinh(sqrt((1 / self.om - 1) / (1 + z)**3))


