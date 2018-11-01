#include <vector>
#include <RTIMULib.h>
#include <RTMath.h>
#include "FIR.h"


typedef struct {
	double x, y, z;
} imu_vector_t;

typedef struct {
	imu_vector_t acc, gyr, mag;
	double qw, qx, qy, qz;
	double roll, pitch, yaw;
} imu_data_t;

class LSM9DS0 {
public:
    LSM9DS0();
    ~LSM9DS0();

    imu_data_t read();
    int getPollInterval();
    	 
private:
    RTIMUSettings *settings;
    RTIMU *imu;
    FIR fir_roll;
    FIR fir_pitch;
    FIR fir_yaw;
    
 };
