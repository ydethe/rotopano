import time

import numpy as np
from .imu_driver import LSM9DS0
from SystemControl.Sensors import ASensors


class IMU (ASensors):
    def __init__(self):
        moy = np.zeros(3)
        cov = np.zeros((3,3))
        ASensors.__init__(self, ['roll','pitch','yaw'], moy, cov)
        self._imu = LSM9DS0()
        
    def behavior(self, x, u, t):
        data = self._imu.read()
        res = np.array([data.roll,data.pitch,data.yaw])

        return res



