#include <vector>
#include <RTIMULib.h>


class LSM9DS0 {
public:
    LSM9DS0();
    ~LSM9DS0();

    std::vector<double> read();
    	 
private:
    RTIMUSettings *settings;
	 RTIMU *imu;
	 std::vector<double> toReturn;
};
