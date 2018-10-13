/* File: example.i */
%module imu_driver

%{
#define SWIG_FILE_WITH_INIT
#include "lsm9ds0_yann.h"
%}

%include "lsm9ds0_yann.h"

