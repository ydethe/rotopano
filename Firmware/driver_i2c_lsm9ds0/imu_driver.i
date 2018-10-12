/* File: example.i */
%module imu_driver

%include "typemaps.i"
%include "std_vector.i"

namespace std {
   %template(DoubleVector) vector<double>;
}
	
%{
#define SWIG_FILE_WITH_INIT
#include "lsm9ds0_yann.h"
%}

%include "lsm9ds0_yann.h"

