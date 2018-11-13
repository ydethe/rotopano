#include <iostream>
#include <vector>
#include <stdint.h>
#include <RTIMULib.h>
#include "lsm9ds0_yann.h"


LSM9DS0::LSM9DS0() {
    //  using RTIMULib here allows it to use the .ini file generated by RTIMULibDemo.
	 settings = new RTIMUSettings("RTIMULib");

    imu = RTIMU::createIMU(settings);

    if ((imu == NULL) || (imu->IMUType() == RTIMU_TYPE_NULL)) {
        printf("No IMU found\n");
        exit(1);
    }

    //  This is an opportunity to manually override any settings before the call IMUInit

    //  set up IMU
    imu->IMUInit();

    //  this is a convenient place to change fusion parameters
    imu->setSlerpPower(0.02);
    imu->setGyroEnable(true);
    imu->setAccelEnable(true);
    imu->setCompassEnable(false);

    fir_pitch = FIR();
    fir_pitch.lowpass(32, 0.05);

    fir_roll = FIR();
    fir_roll.lowpass(32, 0.05);

    fir_yaw = FIR();
    fir_yaw.lowpass(32, 0.05);

 }

 LSM9DS0::~LSM9DS0() {
 }

imu_data_t LSM9DS0::read() {
    imu->IMURead();
	RTIMU_DATA imuData = imu->getIMUData();
	imu_data_t res;

	res.gyr.x = imuData.gyro.x();
	res.gyr.y = imuData.gyro.y();
	res.gyr.z = imuData.gyro.z();

	res.acc.x = imuData.accel.x();
	res.acc.y = imuData.accel.y();
	res.acc.z = imuData.accel.z();

	res.mag.x = imuData.compass.x();
	res.mag.y = imuData.compass.y();
	res.mag.z = imuData.compass.z();
	/*
	res.roll = fir_roll.filter(imuData.fusionPose.x());
	res.pitch = fir_pitch.filter(imuData.fusionPose.y());
	res.yaw = fir_yaw.filter(imuData.fusionPose.z());
	*/
	res.roll  = res.raw_roll;
	res.pitch = res.raw_pitch;
	res.yaw   = res.raw_yaw;

	res.raw_roll = imuData.fusionPose.x();
	res.raw_pitch = imuData.fusionPose.y();
	res.raw_yaw = imuData.fusionPose.z();

	res.qx = imuData.fusionQPose.x();
	res.qy = imuData.fusionQPose.y();
	res.qz = imuData.fusionQPose.z();
	res.qw = imuData.fusionQPose.scalar();

	return res;

}

int LSM9DS0::getPollInterval() {
    return imu->IMUGetPollInterval();
}
