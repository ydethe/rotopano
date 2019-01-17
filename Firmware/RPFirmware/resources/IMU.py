from collections import namedtuple
import os

from singleton3 import Singleton

from imu_driver import LSM9DS0


class IMU (object, metaclass=Singleton):
    def __init__(self):
        self.imu = LSM9DS0()
            
    def read(self) -> "imu_data_t":
        return self.imu.read()
        
    def getPollInterval(self) -> "int":
        return self.imu.getPollInterval()
        
        
        