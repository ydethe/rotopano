import numpy as np

from SystemControl.Sensors import ASensors


class RPSensors (ASensors):
    def __init__(self):
        m = np.zeros(4)
        m[1] = np.pi/180
        m[3] = -3.*np.pi/180
        cov = np.zeros((4,4))
        cov[0,0] = 0.00161054434983
        cov[1,1] = 0.0361459703189
        cov[2,2] = 0.00161054434983
        cov[3,3] = 0.0836563152247
        ASensors.__init__(self, name_of_mes=['tilt_mes','vtilt_mes','pan_mes', 'vpan_mes'], mean=m, cov=cov)
        
    def behavior(self, x, u, t):
        pan, tilt = x
        cmd_vpan, cmd_vtilt = u
        mes = np.array([pan, cmd_vpan, tilt, cmd_vtilt])
        return mes
        