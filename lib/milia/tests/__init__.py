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

'''Unit testing for pymilia package'''

def isclose(x, y, rtol=1.e-5, atol=1.e-8):
    return abs(x-y) <= atol + rtol * abs(y)

def nat_distance(model):
    res = []
    for param, checktup in model:
        hubble_radius = 299792.458 / param[0]
        aa = param[1:]
        bb = [(d / hubble_radius ,z,_tol) for d, z, _tol in checktup]
        res.append((aa, bb))
    return res

def nat_age(model):
    res = []
    for param, checktup in model:
        hubble_time = 977.792222 / param[0]
        aa = param[1:]
        bb = [(d / hubble_time ,z,_tol) for d, z, _tol in checktup]
        res.append((aa, bb))
    return res

def nat_volume(model):
    res = []
    for param, checktup in model:
        hubble_radius = 299792.458 / param[0]
        aa = param[1:]
        bb = [(d / hubble_radius**3 ,z,_tol) for d, z, _tol in checktup]
        res.append((aa, bb))
    return res

model = {}

model['lum'] = [([50., 0.0, 0.0], # OM_OV_0
            [[5.99884708458, 0.001, 1e-7], # OM_OV_0
            [60.258284058, 0.01, 1e-6],
            [629.5641618, 0.1, 1e-3],
            [8993.77374, 1, 1e-1],
            [359750.9496, 10, 1e-3]]),
            ([70., 0.3, 0.7], # OM_OV_1
            [[4.28606, 0.001, 1e-5], # OM_OV_1
            [43.1582, 0.01, 1e-4],
            [460.299, 0.1, 1e-3],
            [6607.65, 1, 1e-2],
            [103843, 10, 1]]),
            ([50., 0.0, 0.5], # OM
            [[6.00034529785633, 0.001, 1e-5], # OM
            [60.4074354667724, 0.01, 1e-4],
            [643.848885216858, 0.1, 1e-3],
            [10045.7135751853, 1, 1e-2],
            [420755.759629146, 10, 1e-1]]),
            ([50., 0.0, 1.0], # OM_DS
            [[6.00184500916, 0.001, 1e-5], # OM_DS
            [60.558076516, 0.01, 1e-4],
            [659.5434076, 0.1, 1e-3],
            [11991.69832, 1, 1e-2],
            [659543.4076, 10, 1e-1]]),
            ([50., 0.5, 0.],  # OV_1
            [[5.99809, 0.001, 1e-5], # OV_1
            [60.1827, 0.01, 1e-4],
            [621.524, 0.1, 1e-3],
            [7812.96, 1, 1e-2],
            [135543., 10, 1]]),
            # [50., 1.5, 0.], # OV_2 makes the Universe recollapse
            ([50., 1.0, 0.], # OV_EDS
            [[5.99734, 0.001, 1e-5], # OV_EDS
            [60.1076, 0.01, 1e-4],
            [613.868, 0.1, 1e-3],
            [7024.57, 1, 1e-2],
            [92136.7, 10, 1e-1]]),
            ([50., 0.3, 0.2], # A1
            [[5.99899, 0.001, 1e-5], # A1
            [60.2722, 0.01, 1e-4],
            [630.081, 0.1, 1e-3],
            [8470.22, 1, 1e-2],
            [168260., 10, 1]])
            # [50., 1.5, 0.008665856], // A2_1 recollapse
            # [50., 1.5, 0.007],    // A2_2
]

model['ang'] = [((50, 1.0, 0.0),
            [(5.98537, 0.001, 1e-5), (58.9232, 0.01, 1e-4), (507.329, 0.1, 1e-3), (1756.14, 1, 1e-2), (761.460, 10, 1e-3)])]

model['cotran'] = [((50., 1.0, 0.), [(5.99135, 0.001, 1e-5),
				    (59.5125, 0.01, 1e-4),
    				(558.062, 0.1, 1e-3),
                    (3512.28, 1, 1e-2),
                    (8376.05, 10, 1e-1)])]


model['com'] = [
    ((50., 1.0, 0.), [(5.99135, 0.001, 1e-5),
                     (59.5125, 0.01, 1e-4),
                   (558.062, 0.1, 1e-3),
                   (3512.28, 1, 1e-2),
                    (8376.05, 10, 1e-1)]),
    ((50., 0.5, 0.6), [(5.99390, 0.001, 1e-5),
       (59.7635, 0.01, 1e-4),
       (580.027, 0.1, 1e-3),
       (4275.74, 1, 1e-2),
       (11212.1, 10, 1e-1)]),
    ((50., 0.5, 0.4), [(5.99330, 0.001, 1e-5),
       (59.7042, 0.01, 1e-4),
       (574.702, 0.1, 1e-3),
       (4085.51, 1, 1e-2),
       (10714.2, 10, 1e-1)])
    ]

model['age'] = [((50., 0.0, 0.0), # OM_OV_0
                [(19.55584444, 0,1e-2),
                 (17.7780, 0.1, 1e-4),
                 (9.77792222, 1, 1e-2),
                 (1.77780, 10, 1e-5),
                 (0.193622, 100, 1e-5)]),
    ((70., 0.3, 0.7), # OM_OV_1
[(13.4669, 0, 1e-4), 
  (12.1656, 0.1, 1e-4),
  (5.75164, 1, 1e-5),
  (0.465887, 10, 1e-6),
  (0.0167499, 100, 1e-7)]),
    ((50., 0.0, 0.5), # OM
            [(24.3753, 0, 1e-4),
            (22.5565, 0.1, 1e-4),
            (13.3084, 1, 1e-4),
            (2.51074, 10, 1e-5),
            (0.273818, 100, 1e-6)]),
    ((50., 0.5, 0.), # OV_1
        [(14.7362, 0, 1e-4),
          (12.9794, 0.1, 1e-4),
          (5.73993, 1, 1e-5),
          (0.492223, 10, 1e-6),
          (0.0181106, 100, 1e-7)]),
    ((50., 1.0, 0.), # OV_3
         [(13.037229, 0, 1e-2),  
          (11.3004, 0.1, 1e-4),
          (4.60935, 1, 1e-5),
          (0.357352, 10, 1e-6),
          (0.0128440, 100, 1e-7)]),
    ((50., 0.3, 0.2), # A1
        [(16.5055784617336, 0, 1e-4), 
          (14.7250045860962, 0.1, 1e-4),
          (6.87687623769365, 1, 1e-5),
          (0.624924600328037, 10, 1e-6),
          (0.0233349119803707, 100, 1e-7)]),
    ((70., 0.23, 0.73), # A1, direct integration
[(14.2684, 0, 1e-4), 
  (12.9629, 0.1, 1e-4),
  (6.33995, 1, 1e-5),
  (0.529525558080137, 10, 1e-6),
  (0.0191199557036697, 100, 1e-7)]),
]

# (50., 0.3, 1.713460403) breaks
# (50., 0.7, 2.254425343) exception
# (50., 0.7, 3) exception
# (50., 0.3, 2.) exception


model['vol'] = [
    ((50., 0.5, 0.),[
    (71.7161408548458, 1e-3, 1e-1),
    (70522.0339930576, 1e-2, 1e3),
    (60047832.08635, 1e-1, 1e4),
    (18733087921.7912, 1 , 1e5),
    (425218980174.27, 10, 1e6),
  ]),
    ((71., 0.31, 0.70), [
    (25.0766380119768,1e-3,1e-1),
    (24922.5144468078,1e-2,1e3),
    (23387784.8229885,1e-1,1e5),
    (11406084150.5617,1,1e5),
    (259503559696.949,10,1e6)]),
    ((50., 1.0, 0.), [(71.6892647166395,1e-3,1e-4),
	  (70259,1e-2,1),
	  (5.79331e+07,1e-1,1e2),
	  (1.44427e+10,1,1e5),
	  (1.95883e+11,10,1e6)]),
    ((71., 0.27, 0.73), [(25.078518575672,1e-3,1e-4),
	  (24941.2341109484,1e-2,1),
	  (23565185.7509809,1e-1,1e2),
	  (12169565883.3662,1,1e5),
	  (300884961157.615,10,1e6)])
]

# Convert function to apply to each model
_apply = {'vol': nat_volume, 'ang': nat_distance, 'lum': nat_distance,
        'age': nat_age, 'com': nat_distance, 'cotran': nat_distance}

model_nat = {}

for key in model:
    model_nat[key] = _apply[key](model[key])

