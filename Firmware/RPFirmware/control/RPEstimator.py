import numpy as np

from SystemControl.Estimator import AKalmanFilter


class RPEstimator (AKalmanFilter):
    def __init__(self, controller):
        AKalmanFilter.__init__(self, ['pan_est','bais_vpan_est','tilt_est','biais_vtilt_est'], controller)
        self.reset()

    def reset(self):
        self.setState(np.zeros(4))
        self.setStateCovariance(np.eye(4))

    def A(self, t1, t2):
        return np.eye(4)

    def B(self, t1, t2):
        return np.array([[t2-t1,0],[0,0],[0,t2-t1],[0,0]])

    def C(self, t1, t2):
        return np.eye(4)

    def D(self, t1, t2):
        return np.array([[0,0],[1,0],[0,0],[0,1]])

    def Q(self, t1, t2):
        return np.zeros((4,4))

    def R(self, t1, t2):
        R = np.zeros((4,4))
        R[0,0] = 0.00161054434983
        R[1,1] = 0.0361459703189
        R[2,2] = 0.00161054434983
        R[3,3] = 0.0836563152247
        return R
