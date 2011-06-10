/*
 * Copyright 2008-2011 Sergio Pascual
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


#include <boost/python.hpp>
#include <milia/flrw.h>
#include <milia/flrw_nat.h>
#include <milia/exception.h>

using milia::metrics::flrw;
using milia::metrics::flrw_nat;

double (flrw::*age0)() const = &flrw::age;
double (flrw::*age1)(double) const = &flrw::age;
double (flrw_nat::*a_age0)() const = &flrw_nat::age;
double (flrw_nat::*a_age1)(double) const = &flrw_nat::age;
double (flrw_nat::*a_dc)(double) const = &flrw_nat::dc;
double (flrw_nat::*a_da)(double) const = &flrw_nat::da;
double (flrw_nat::*a_dm)(double) const = &flrw_nat::dm;
double (flrw_nat::*a_vol)(double) const = &flrw_nat::vol;

double (flrw::*gh)() const = &flrw::get_hubble;
double (flrw::*gm)() const = &flrw::get_matter;
double (flrw::*gv)() const = &flrw::get_vacuum;

double (flrw::*a_gm)() const = &flrw_nat::get_matter;
double (flrw::*a_gv)() const = &flrw_nat::get_vacuum;


void translate(milia::exception const& e) {
	// Use the Python 'C' API to set up an exception object
	PyErr_SetString(PyExc_UserWarning, e.what());
}

BOOST_PYTHON_MODULE(_milia) {
	using namespace boost::python;

	scope().attr("__doc__") = "Metrics that are solutions of Einstein's equations.\n"
	    "\n"
	    "This module contains the Friedman-Lemaitre-Robertson-Walker (Flrw) metric\n";


	class_<flrw>("Flrw", "The Friedmann-Lemaitre-Robertson-Walker metric\n"
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
	.def("dl", &flrw::dl,
			args("redshift"),
			"Return the luminosity distance in Mpc."
	)
	.def("dc", &flrw::dc,
			args("redshift"),
			"Return the comoving distance in the line of sight in Mpc."
	)
	.def("dm", &flrw::dm,
			args("redshift"),
			"Return the comoving distance in the transverse direction in Mpc."
	)
	.def("da", &flrw::da,
			args("redshift"),
			"Return the angular distance in Mpc."
	)
	.def("lt", &flrw::lt,
			args("redshift"),
			"Return the look-back time in Gyr."
	)
	.def("vol", &flrw::vol,
			args("redshift"),
			"Return the comoving volume per solid angle in Mpc^3 / sr"
	)
	.def("age", age0, args(""),
			"Return the current age of the Universe (at redshift 0) in Gyr."
	)
    .def("angular_scale", &flrw::angular_scale, args("redshift"),
			"Return the factor to transform angular sizes in pc / arc sec."
	)
	.def("age", age1, args("redshift"), "Return the age of the Universe in Gyr.")
	.def("hubble_radius", &flrw::hubble_radius, args(""),
			"Return the Hubble radius in Mpc.")
	.def("hubble_time", &flrw::hubble_time, args(""),
			"Return the Hubble time in Gyr.")
	//.def(str(self))
    .def("__str__", &flrw::to_string)
    .add_property("hubble", gh, &flrw::set_hubble)
    .add_property("matter", gm, &flrw::set_matter)
    .add_property("vacuum", gv, &flrw::set_vacuum)
	;

	class_<flrw_nat>("FlrwNat", "The Friedmann-Lemaitre-Robertson-Walker metric in natural units\n"
	    "\n"
	    "This class represents a FLRW metric in natural units. Its methods compute the\n"
	    "common cosmological distances and times.",
	    init<double, double>("Create a FlrwNat object.\n"
	        "\n"
	        "The constructor takes two parameters:\n"
	        "matter density (adimensional)\n"
	        "vacuum energy density (adimensional)",
	        (args("matter"),args("vacuum"))))
	.def("dl", &flrw_nat::dl,
			args("redshift"),
			"Return the adimensional luminosity distance."
	)
	.def("dc", a_dc,
			args("redshift"),
			"Return the adimensional comoving distance in the line of sight."
	)
	.def("dm", a_dm,
			args("redshift"),
			"Return the adimensional comoving distance in the transverse direction."
	)
	.def("da", a_da,
			args("redshift"),
			"Return the adimensioanl angular distance."
	)
	.def("lt", &flrw_nat::lt,
			args("redshift"),
			"Return the adimensional look-back time."
	)
	.def("vol", a_vol,
			args("redshift"),
			"Return the adimensional comoving volume per solid angle."
	)
	.def("age", a_age0, args(""),
			"Return the adimensional current age of the Universe (at redshift 0)."
	)
	.def("age", a_age1, args("redshift"), "Return the adimensional age of the Universe.")
    .def("hubble", &flrw_nat::hubble, args("redshift"),
    		"Return adimensional Hubble parameter.")
	//.def(str(self))
    .def("__str__", &flrw_nat::to_string)
    .add_property("matter", a_gm, &flrw_nat::set_matter)
    .add_property("vacuum", a_gv, &flrw_nat::set_vacuum)
	;

	register_exception_translator<milia::exception>(&translate);
}
