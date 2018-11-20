import numpy as np

from SystemControl.Estimator import KalmanFilter


class RPEstimator (KalmanFilter):
    def __init__(self):
        KalmanFilter.__init__(self, name_of_states=['pan_est','bais_vpan_est','tilt_est','biais_vtilt_est'])
        Q = np.zeros((4,4))
        R = np.zeros((4,4))
        R[0,0] = 0.00161054434983
        R[1,1] = 0.0361459703189
        R[2,2] = 0.00161054434983
        R[3,3] = 0.0836563152247
        self.setMatrices(A=lambda t1, t2:np.eye(4),
                         B=lambda t1, t2:np.array([[t2-t1,0],[0,0],[0,t2-t1],[0,0]]),
                         C=lambda t1, t2:np.eye(4),
                         D=lambda t1, t2:np.array([[0,0],[1,0],[0,0],[0,1]]),
                         Q=lambda t1, t2:Q,
                         R=lambda t1, t2:R)
        self.reset()

    def reset(self):
        self.setEstimation(np.zeros(4),np.eye(4),0.)
