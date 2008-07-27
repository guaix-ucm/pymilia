// $Id: emir_wrap.cc 321 2008-07-22 19:32:33Z spr $

#include <milia/metric.h>
#include <milia/exception.h>

#include <boost/python.hpp>

/*
void (EMIR::TestData::*show)() const = &EMIR::TestData::show;
void (EMIR::TestData::*set)(const std::string&) = &EMIR::TestData::set;
void (EMIR::TestFilter::*run1)() const = &EMIR::TestFilter::run;
double (EMIR::TestFilter::*run2)(int) const = &EMIR::TestFilter::run;
EMIR::TestData (EMIR::TestFilter::*run3)(const EMIR::TestData&) const = &EMIR::TestFilter::run;
*/

void translate(milia::exception const& e)
{
    // Use the Python 'C' API to set up an exception object
    PyErr_SetString(PyExc_RuntimeError, e.what());
}

BOOST_PYTHON_MODULE(pymilia) {
  using namespace boost::python;
	class_<milia::metric>("metric", init<double, double, double>())
	;
	class_<milia::exception>("exception", "docstring")
	;
  register_exception_translator<milia::exception>(&translate);
}
