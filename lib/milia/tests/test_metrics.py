#
# Copyright 2009-2011 Sergio Pascual
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

import unittest

from milia.metrics import Flrw

def isclose(x, y, rtol=1.e-5, atol=1.e-8):
    return abs(x-y) <= atol + rtol * abs(y)

lum_table = [[[5.99884708458, 0.001, 1e-7], 
         [60.258284058, 0.01, 1e-6],
         [629.5641618, 0.1, 1e-3],
         [8993.77374, 1, 1e-1],
         [359750.9496, 10, 1e-3]],
        [[4.28606, 0.001, 1e-5], 
         [43.1582, 0.01, 1e-4],
         [460.299, 0.1, 1e-3],
         [6607.65, 1, 1e-2],
         [103843, 10, 1]],
        [[6.00034529785633, 0.001, 1e-5], 
             [60.4074354667724, 0.01, 1e-4],
      [643.848885216858, 0.1, 1e-3],
       [10045.7135751853, 1, 1e-2],
          [420755.759629146, 10, 1e-1]],
       [[6.00184500916, 0.001, 1e-5], 
        [60.558076516, 0.01, 1e-4],
         [659.5434076, 0.1, 1e-3],
       [11991.69832, 1, 1e-2],
        [659543.4076, 10, 1e-1]],
        [[5.99809, 0.001, 1e-5], # OV_1
         [60.1827, 0.01, 1e-4],
           [621.524, 0.1, 1e-3],
            [7812.96, 1, 1e-2],
         [135543., 10, 1]],
        [[5.99734, 0.001, 1e-5], # OV_EDS
         [60.1076, 0.01, 1e-4],
        [613.868, 0.1, 1e-3],
        [7024.57, 1, 1e-2],
        [92136.7, 10, 1e-1]],
       [[5.99899, 0.001, 1e-5], # A1
        [60.2722, 0.01, 1e-4],
        [630.081, 0.1, 1e-3],
        [8470.22, 1, 1e-2],
        [168260., 10, 1]]]

lum_model = [
    [50., 0.0, 0.0], # OM_OV_0
    [70., 0.3, 0.7], # OM_OV_1
    [50., 0.0, 0.5], # OM
    [50., 0.0, 1.0], # OM_DS
    [50., 0.5, 0.],  # OV_1
    # [50., 1.5, 0.], # OV_2 makes the Universe recollapse
    [50., 1.0, 0.], # OV_EDS
    [50., 0.3, 0.2], # A1
    # [50., 1.5, 0.008665856], // A2_1 recollapse
    # [50., 1.5, 0.007],    // A2_2
   ]

ang_model = [((50, 1.0, 0.0),((5.98537, 0.001, 1e-5), (58.9232, 0.01, 1e-4), (507.329, 0.1, 1e-3), (1756.14, 1, 1e-2), (761.460, 10, 1e-3)))]

class FlrwTest(unittest.TestCase):

    def test_luminosity_distance(self):
        for idx, (h,m,l) in enumerate(lum_model):
            mm = Flrw(h, m, l)
            for d, z, _tol in lum_table[idx]:
                self.assertTrue(isclose(mm.dl(z), d))
    
    def test_angular_distance(self):
        for param, checktup in ang_model:
            mm = Flrw(*param)
            for d, z, _tol in checktup:                
                self.assertTrue(isclose(mm.da(z), d))

    def test_comoving_transverseDistance(self):
        self.assertTrue(True)
    
    def test_comoving_distance(self):
        self.assertTrue(True)
    
    def test_age(self):
        self.assertTrue(True)
    
    def test_comoving_volume(self):
        self.assertTrue(True)
    
def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FlrwTest))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
