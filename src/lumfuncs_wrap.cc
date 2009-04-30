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

#include <boost/python.hpp>
#include <boost/python/tuple.hpp>
#include <boost/lambda/lambda.hpp>
#include <milia/schechter.h>

namespace lf = milia::luminosity_functions;
namespace py = boost::python;
namespace lbd = boost::lambda;


typedef boost::tuple<double, double, double> Tuple3Type;


namespace my
{
  // Converts a boost::tuple of 3 double into a python tuple
  py::tuple tuple_to_python(Tuple3Type const& x)
  {
    return py::make_tuple(x.get<0> (), x.get<1> (), x.get<2> ());
  }

  // Struct needed to register the converter
  struct tuple3_to_python
  {
      static PyObject* convert(const Tuple3Type& tuple3)
      {
        return py::incref(my::tuple_to_python(tuple3).ptr());
      }
  };
}

BOOST_PYTHON_MODULE(lumfuncs)
{
  using namespace boost::python;

  // Registers the tuple conversion
  to_python_converter<Tuple3Type, my::tuple3_to_python> ();

  scope().attr("__doc__") = "lumfuncs' docstring";

  class_<lf::schechter> ("Schechter", init<double, double, double> ())
  .def(init<double, double, double, double, double, double, double> ())
  .def("evolve", &lf::schechter::evolve, args("redshift"), "evolve the luminosity function")
  .def("function", &lf::schechter::function)
  .def("object_density", &lf::schechter::object_density)
  //.def("luminosity_density", &lf::schechter::luminosity_density)
  .def("parameters", &lf::schechter::parameters)
  //.def(str(self))
  .def("__str__",&lf::schechter::to_string)
  ;

}
