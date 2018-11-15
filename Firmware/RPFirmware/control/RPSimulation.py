import numpy as np

from SystemControl.Simulation import ASimulation


class RPSimulation (ASimulation):
    def __init__(self, cons, dt, ctrl, sys, sensors, estimator):
        ASimulation.__init__(self, dt, ctrl, sys, sensors, estimator)
        self._cons = cons
        
    def behavior(self, xest, t):
        if t < 10:
            return self._cons
        else:
            return np.zeros(2)
        