
Using PyMilia
========================

Standard metric
---------------

PyMilia provides a class representing the standard 
`Friedmann–Lemaître–Robertson–Walker <http://en.wikipedia.org/wiki/Friedmann%E2%80%93Lema%C3%AEtre%E2%80%93Robertson%E2%80%93Walker_metric>`_ metric. The 
class is named :py:class:`.Flrw`. The name :py:class:`.Metric` can also 
be used. 

One starts initializing the metric passing the values of the Hubble parameter,
the matter density and the vaccum density to the constructor. The distance
units are megaparsec, time units are gigayear::

  >>> from milia import Flrw
  >>> metric = Flrw(73, 0.27, 0.73)

Once the metric is created, we can compute different distances, volumes and
ages at a given redshift. For example, the luminosity distance at redshift
1.5. Distance units are megaparsec::

  >>> metric.dl(1.5)
  10708.524358401042


We can compute also age and look-back time. For example, the look-back time
at the same redshift.::

  >>> metric.lt(1.5)
  9.06546678715405


===============================  =====================
Measurement                      Method
===============================  =====================
Comoving distance                :py:meth:`.Flrw.dc`
Comoving distance (transverse)   :py:meth:`.Flrw.dm`
Angular distance                 :py:meth:`.Flrw.da` 
Luminosity distance              :py:meth:`.Flrw.dl`
Comoving volume                  :py:meth:`.Flrw.vol`
Age                              :py:meth:`.Flrw.age`
Look-back time                   :py:meth:`.Flrw.lt`
===============================  =====================
