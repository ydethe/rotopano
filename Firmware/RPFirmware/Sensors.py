import time

import numpy as np
from .imu_driver import LSM9DS0
from libSystemControl.Sensors import ASensors


class IMU (ASensors):
    def __init__(self):
        moy = np.zeros(9)
        cov = np.zeros((9,9))
        ASensors.__init__(self, ['gx_mes','gy_mes','gz_mes','ax_mes','ay_mes','az_mes', 'mx_mes', 'my_mes', 'mz_mes'], moy, cov)
        self._imu = LSM9DS0()
        
    def behavior(self, x, u, t):
        data = self._imu.read()
        gyr,mag,acc = data.gyr,data.mag,data.acc
        res = np.array([gyr.x,gyr.y,gyr.z,acc.x,acc.y,acc.z,mag.x,mag.y,mag.z])

        return res



