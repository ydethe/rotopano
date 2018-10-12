import imu_driver


a = imu_driver.LSM9DS0()
print(a.read())
