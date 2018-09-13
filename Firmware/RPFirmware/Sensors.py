import time

import numpy as np
from .LSM9DS0 import LSM9DS0
from libSystemControl.Sensors import ASensors


class IMU (ASensors):
    def __init__(self):
        moy = np.zeros(9)
        cov = np.zeros((9,9))
        ASensors.__init__(self, ['gx_mes','gy_mes','gz_mes','ax_mes','ay_mes','az_mes', 'mx_mes', 'my_mes', 'mz_mes'], moy, cov)
        self._imu = LSM9DS0()
        
    def behavior(self, x, u, t):
        data = self._imu.read()
        gyr,mag,acc = data
        res = np.array([gyr[0],gyr[1],gyr[2],acc[0],acc[1],acc[2],mag[0],mag[1],mag[2]])

        return res



