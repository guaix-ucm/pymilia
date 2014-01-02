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

# NonFlat models

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

    def age(self, z):
        return math.asinh(1 / ((1 + z) * math.sqrt(1 / self.ov - 1))) / math.sqrt(self.ov)

class Flrw_OV(FlrwNonFlat):
    def __init__(self, matter):
        super(Flrw_OV, self).__init__(matter, 0.0)

        self.pre0 = 1 - matter

    def pre(self, z):
        return math.sqrt(1 + self.om * z)

    def dl(self, z):
        return 2 * ((2 - self.om * (1 - z) - (2 - self.om) * math.sqrt(1 + self.om * z))) / (self.om * self.om)

class Flrw_OV_1(Flrw_OV):
    def __init__(self, matter):
        super(Flrw_OV_1, self).__init__(matter)

    def age(self, z):
        prez = self.pre(z)
        return (prez / (1 + z) - self.om / math.sqrt(pre0) * math.atanh(math.sqrt(pre0) / prez)) / pre0

class Flrw_OV_2(Flrw_OV):
    def __init__(self, matter):
        super(Flrw_OV_2, self).__init__(matter)

    def age(self, z):
        prez = self.pre(z)
        return (prez / (1 + z) - self.om / math.sqrt(-pre0) * math.atan(math.sqrt(-pre0) / prez)) / pre0
        

class FlrwA(FlrwNonFlat):
    def __init__(self, matter, vacuum, crit):
        super(FlrwA, self).__init__(matter, vacuum)
        self.crit = crit

class FlrwA1(FlrwA):
    def __init__(self, matter, vacuum, crit):
        super(FlrwA1, self).__init__(matter, vacuum, crit)

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
        super(FlrwA2_1, self).__init__(matter, vacuum, 2.0)

class FlrwA2_2(FlrwA2):
    def __init__(self, matter, vacuum, crit):
        super(FlrwA2_2, self).__init__(matter, vacuum, crit)

