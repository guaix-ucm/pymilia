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

import unittest

from milia import Flrw
from milia.tests import isclose, model

class FlrwTest(unittest.TestCase):

    def test_luminosity_distance(self):
        for param, checktup in model['lum']:
            mm = Flrw(*param)
            for d, z, _tol in checktup:                
                self.assertTrue(isclose(mm.dl(z), d))
    
    def test_angular_distance(self):
        for param, checktup in model['ang']:
            mm = Flrw(*param)
            for d, z, _tol in checktup:                
                self.assertTrue(isclose(mm.da(z), d))

    def test_comoving_transverse_distance(self):
        for param, checktup in model['cotran']:
            mm = Flrw(*param)
            for d, z, _tol in checktup:                
                self.assertTrue(isclose(mm.dm(z), d))
    
    def test_comoving_distance(self):
        for param, checktup in model['com']:
            mm = Flrw(*param)
            for d, z, _tol in checktup:                
                self.assertTrue(isclose(mm.dc(z), d))
    
    @unittest.skip("not implemented yet")
    def test_age(self):
        for param, checktup in model['age']:
            mm = Flrw(*param)
            for d, z, _tol in checktup:
                self.assertTrue(isclose(mm.age(z), d))
                
    
    def test_comoving_volume(self):
        for param, checktup in model['vol']:
            mm = Flrw(*param)
            for d, z, _tol in checktup:
                self.assertTrue(isclose(mm.vol(z), d))
    
def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FlrwTest))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
