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

#include <milia/schechter.h>

namespace lf = milia::luminosity_functions;
namespace py = boost::python;

typedef boost::tuple<double, double, double> Tuple3Type;

namespace my
{
  // Converts a boost::tuple of 3 double into a python tuple
  py::tuple tuple_to_python(Tuple3Type const& x)
  {
    return py::make_tuple(x.get<0>(), x.get<1>(), x.get<2>());
  }

  // Struct needed to register the converter
  struct tuple3_to_python
  {
      static PyObject* convert(const Tuple3Type& tuple3)
      {
        return py::incref(my::tuple_to_python(tuple3).ptr());
      }
  };

  class pyobject_func_wrapper
  {
    public:
      pyobject_func_wrapper(py::object& obj) :
        m_obj_(obj)
      {
      }

      double operator()(double z)
      {
        return py::extract<double>(m_obj_(z));
      }

      private:
      py::object& m_obj_;
    };

    double foo(py::object fp)
    {
      return py::extract<double>(fp(0.1));
    }

    class PySchechter : public lf::schechter
    {
      public:
      PySchechter(py::object phi, py::object lum, py::object alpha, double z) :
      lf::schechter(pyobject_func_wrapper(phi), pyobject_func_wrapper(lum),
          pyobject_func_wrapper(alpha), z)
      {
      }

    };

/*    class<...>(...)
    .def("__str__", boost::lexical_cast<std::string, MyClass const &>)

    if MyClass is streamable. If it's not, you can always do something
    totally custom:*/


    static std::string schechter__str__(lf::schechter const &self)
    {
      return std::string("Whatever I want.");
    }

  }

  BOOST_PYTHON_MODULE(lumfuncs)
  {
    using namespace boost::python;

    // Registers the tuple conversion
    to_python_converter<Tuple3Type, my::tuple3_to_python>();

    scope().attr("__doc__") = "lumfuncs' docstring";

    class_<lf::schechter>("Schechter", init<double, double, double, double>())
    /* this construct doesn't work */
    /*.def(init<boost::function<double(double)>,
     boost::function<double(double)>,
     boost::function<double(double)>, double>())*/
    .def("evolve", &lf::schechter::evolve, args("redshift"),
        "evolve the luminosity function")
    .def("function",&lf::schechter::function)
    .def("object_density",&lf::schechter::object_density)
    .def("luminosity_density", &lf::schechter::luminosity_density)
    .def("parameters", &lf::schechter::parameters)
    .def("__str__", &my::schechter__str__)
    ;

    /*
     * This compiles but segfaults
     class_<PySchechter, bases<lf::schechter> >("PySchechter", init<py::object, py::object, py::object,
     double>());
     */
    def("foo", &my::foo);
  }
