import numpy as np

from SystemControl.Sensors import ASensors
from RPFirmware.ResourcesManager import ResourcesManager


class RPSensors (ASensors):
    def __init__(self):
        m = np.zeros(4)
        # m[1] = np.pi/180
        # m[3] = -3.*np.pi/180
        cov = np.zeros((4,4))
        # cov[0,0] = 0.00161054434983
        # cov[1,1] = 0.0361459703189
        # cov[2,2] = 0.00161054434983
        # cov[3,3] = 0.0836563152247
        ASensors.__init__(self, name_of_mes=['tilt_mes','vtilt_mes','pan_mes', 'vpan_mes'], mean=m, cov=cov)
        self.imu = ResourcesManager().imu

    def behavior(self, x, u, t):
        dat = self.imu.read()

        pan = np.arctan2(dat.acc.z, dat.acc.x)
        vpan = dat.gyr.y

        tilt = np.arctan2(dat.mag.y, dat.mag.x)
        vtilt = dat.gyr.z

        mes = np.array([pan, vpan, tilt, vtilt])
        return mes
