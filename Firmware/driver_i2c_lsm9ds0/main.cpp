#include <stdint.h>
#include <string.h>
#include <iostream>
// #include "lsm9ds0_yann.h"
#include "Adafruit_LSM9DS0.h"
#include "util.h"


int main(int argc, char** argv) {
   gpioInitialise();
   
   initialiseEpoch();
   
   // LSM9DS0 a = LSM9DS0();
   Adafruit_LSM9DS0 a = Adafruit_LSM9DS0();
   
   for (int i=0; i<1000; i++) {
      a.readAccel();
      std::cout << a.accelData.x << "," << a.accelData.y << "," << a.accelData.z << std::endl;
      //std::cout << a.gyroData.x << "," << a.gyroData.y << "," << a.gyroData.z << std::endl;
   }
   
   return 0;
   
}


