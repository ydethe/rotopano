/* File: example.i */
%module imu_driver

%{
#define SWIG_FILE_WITH_INIT

class LSM9DS0 {
public:
   LSM9DS0();

   void readAccel();
   
   typedef struct vector_s
    {
      float x;
      float y;
      float z;
    } lsm9ds0Vector_t;
    
    lsm9ds0Vector_t accelData;    // Last read accelerometer data will be available here
    lsm9ds0Vector_t magData;      // Last read magnetometer data will be available here
    lsm9ds0Vector_t gyroData;     // Last read gyroscope data will be available here
    int16_t         temperature;  // Last read temperzture data will be available here
    
};

%}

#include "lsm9ds0_yann.h"

