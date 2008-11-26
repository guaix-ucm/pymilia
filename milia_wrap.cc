/* 
 * Copyright 2008 Sergio Pascual
 * 
 * This file is part of PyMilia
 * 
 * PyMilia is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * PyMilia is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with PyMilia.  If not, see <http://www.gnu.org/licenses/>.
 * 
 */

// $Id$

#include <milia/metric.h>
#include <milia/exception.h>

#include <boost/python.hpp>

double (milia::metrics::flrw::*age0)() const = &milia::metrics::flrw::age;
double (milia::metrics::flrw::*age1)(double) const = &milia::metrics::flrw::age;
double (milia::metrics::flrw::*dc1)(double) const = &milia::metrics::flrw::dc;
double (milia::metrics::flrw::*dm1)(double) const = &milia::metrics::flrw::dm;
double (milia::metrics::flrw::*da1)(double) const = &milia::metrics::flrw::da;
double (milia::metrics::flrw::*vol1)(double) const = &milia::metrics::flrw::vol;

void translate(milia::exception const& e) {
	// Use the Python 'C' API to set up an exception object
	PyErr_SetString(PyExc_UserWarning, e.what());
}

BOOST_PYTHON_MODULE(milia) {
	using namespace boost::python;
	class_<milia::metrics::flrw>("metric", init<double, double, double>())
	.def("dl", &milia::metrics::flrw::dl,
			args("redshift"),
			"returns the luminosity distance"
	)
	.def("luminosity_distance", &milia::metrics::flrw::dl,
			args("redshift"),
			"returns the luminosity distance"
	)
	.def("dc", dc1,
			args("redshift"),
			"returns the comoving distance in the line of sight"
	)
	.def("dm", dm1,
			args("redshift"),
			"returns the comoving distance in the transverse direction"
	)
	.def("da", da1,
			args("redshift"),
			"returns the angular distance"
	)
	.def("lt", &milia::metrics::flrw::lt,
			args("redshift"),
			"returns the look-back time"
	)
	.def("vol", vol1,
			args("redshift"),
			"returns the comoving volume per solid angle"
	)
	.def("age", age0,args(""),
			"returns the current age of the Universe (at redshift 0)"
	)
	.def("age", age1, args("redshift"), "returns the age of the Universe") ;

	register_exception_translator<milia::exception>(&translate);
}
