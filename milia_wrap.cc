// $Id: emir_wrap.cc 321 2008-07-22 19:32:33Z spr $

#include <milia/metric.h>
#include <milia/exception.h>

#include <boost/python.hpp>

void translate(milia::exception const& e)
{
    // Use the Python 'C' API to set up an exception object
    PyErr_SetString(PyExc_RuntimeError, e.what());
}

BOOST_PYTHON_MODULE(milia) {
  using namespace boost::python;
	class_<milia::metrics::flrw>("metric", init<double, double, double>())
	.def("dl", &milia::metrics::flrw::distance_luminosity)
	;
	class_<milia::exception>("exception", "docstring")
	;
  register_exception_translator<milia::exception>(&translate);
}
