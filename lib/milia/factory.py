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

'''Pure Python implementation of FlrwNat'''

from __future__ import division

from flatmodels import Flrw_OV_EDS, Flrw_OM_DS, Flrw_OM_OV_1
from nonflatmodels import Flrw_OM_OV_0, Flrw_OM, Flrw_OV_1, Flrw_OV_2
from nonflatmodels import FlrwA1, FlrwA2_1, FlrwA2_2

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

