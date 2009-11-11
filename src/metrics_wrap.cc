/*
 * Copyright 2008-2009 Sergio Pascual
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

#include <boost/python.hpp>
#include <milia/metric.h>
#include <milia/exception.h>

namespace mt = milia::metrics;

double (mt::flrw::*age0)() const = &mt::flrw::age;
double (mt::flrw::*age1)(double) const = &mt::flrw::age;
double (mt::flrw::*dc1)(double) const = &mt::flrw::dc;
double (mt::flrw::*dm1)(double) const = &mt::flrw::dm;
double (mt::flrw::*da1)(double) const = &mt::flrw::da;
double (mt::flrw::*vol1)(double) const = &mt::flrw::vol;

void translate(milia::exception const& e) {
	// Use the Python 'C' API to set up an exception object
	PyErr_SetString(PyExc_UserWarning, e.what());
}

BOOST_PYTHON_MODULE(metrics) {
	using namespace boost::python;

	scope().attr("__doc__") = "Metrics that are solutions of Einstein's equations.\n"
	    "\n"
	    "This module contains the Friedman-Lemaitre-Robertson-Walker (Flrw) metric\n";


	class_<mt::flrw>("Flrw", "The Friedmann-Lemaitre-Robertson-Walker metric\n"
	    "\n"
	    "This class represents a FLRW metric. Its methods compute the\n"
	    "common cosmological distances and times.",
	    init<double, double, double>("Create a Flrw object.\n"
	        "\n"
	        "The constructor takes three parameters:\n"
	        "hubble parameter in km / s / Mpc\n"
	        "matter density (adimensional)\n"
	        "vacuum energy density (adimensional)",
	        (args("hubble"),args("matter"),args("vacuum"))))
	.def("dl", &mt::flrw::dl,
			args("redshift"),
			"Return the luminosity distance in Mpc."
	)
	.def("luminosity_distance", &mt::flrw::dl,
			args("redshift"),
			"Return the luminosity distancein Mpc."
	)
	.def("dc", dc1,
			args("redshift"),
			"Return the comoving distance in the line of sight in Mpc."
	)
	.def("dm", dm1,
			args("redshift"),
			"Return the comoving distance in the transverse direction in Mpc."
	)
	.def("da", da1,
			args("redshift"),
			"Return the angular distance in Mpc."
	)
	.def("lt", &mt::flrw::lt,
			args("redshift"),
			"Return the look-back time in Gyr."
	)
	.def("vol", vol1,
			args("redshift"),
			"Return the comoving volume per solid angle in Mpc^3 / sr"
	)
	.def("age", age0, args(""),
			"Return the current age of the Universe (at redshift 0) in Gyr."
	)
    .def("angular_scale", &mt::flrw::angular_scale, args("redshift"),
			"Return the factor to transform angular sizes in pc / arc sec."
	)
	.def("age", age1, args("redshift"), "Return the age of the Universe in Gyr.")
	//.def(str(self))
    .def("__str__", &mt::flrw::to_string)
    .add_property("hubble", &mt::flrw::get_hubble, &mt::flrw::set_hubble)
    .add_property("matter", &mt::flrw::get_matter, &mt::flrw::set_matter)
    .add_property("vacuum", &mt::flrw::get_vacuum, &mt::flrw::set_vacuum)
	;

	register_exception_translator<milia::exception>(&translate);
}
