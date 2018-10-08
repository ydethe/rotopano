#include <stdint.h>
#include <string.h>
#include <iostream>
#include "Adafruit_LSM9DS0.h"


int main(int argc, char** argv) {
   Adafruit_LSM9DS0 a = Adafruit_LSM9DS0();
   
   if (!a.begin()) {
      std::cerr << "Erreur lors de l'appel a begin" << std::endl;
      return 1;
   }
   
   a.read();
   
   std::cout << a.accelData.x << "," << a.accelData.y << "," << a.accelData.z << std::endl;
   
   return 0;
   
}


