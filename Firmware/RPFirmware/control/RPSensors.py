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
        ASensors.__init__(self, 'cpt', [], name_of_states=['pan_mes','vpan_mes','tilt_mes','vtilt_mes'], mean=m, cov=cov)
        self.imu = ResourcesManager().imu

    @ASensors.updatemethod
    # @profile
    def update(self, t1 : float, t2 : float, inputs : dict) -> None:
        dat = self.imu.read()

        tilt = -np.arctan2(-dat.acc.x, -dat.acc.z)
        vtilt = dat.gyr.y
        # print("tilt_mes", tilt*180/np.pi)

        pan = np.arctan2(dat.mag.y, dat.mag.x)
        vpan = -dat.gyr.z

        mes = np.array([pan, vpan, tilt, vtilt])
        self.setState(mes)
