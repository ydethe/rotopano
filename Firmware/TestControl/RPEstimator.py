import numpy as np

from SystemControl.Estimator import KalmanFilter


class RPEstimator (KalmanFilter):
    def __init__(self, dt):
        KalmanFilter.__init__(self, name_of_states=['pan_est','bais_vpan_est','tilt_est','biais_vtilt_est'])
        Q = np.zeros((4,4))
        R = np.zeros((4,4))
        R[0,0] = 0.00161054434983
        R[1,1] = 0.0361459703189
        R[2,2] = 0.00161054434983
        R[3,3] = 0.0836563152247
        self.setMatrices(np.eye(4),np.array([[dt,0],[0,0],[0,dt],[0,0]]),np.eye(4), np.array([[0,0],[1,0],[0,0],[0,1]]),Q,R,dt)
        self.reset()
        
    def reset(self):
        self.setEstimation(np.zeros(4),np.eye(4),0.)
        