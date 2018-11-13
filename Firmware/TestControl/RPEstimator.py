from SystemControl.Estimator import KalmanFilter


class RPEstimator (KalmanFilter):
    def __init__(self):
        KalmanFilter.__init__(self,name_of_states=['tilt_est','pan_est'])
        self.setMatrices(A, B, C, D, Q, R, dt)
