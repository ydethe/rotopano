import numpy as np

from SystemControl.Simulation import ASimulation
from RPFirmware.Observe import Observer


class RPSimulation (ASimulation, Observer):
    def __init__(self, dt, ctrl, sys, sensors, estimator):
        ASimulation.__init__(self, dt, ctrl, sys, sensors, estimator)
        self._cons = np.zeros(2)

    def setConsigne(self, cons):
        self._cons = cons

    def handleMsg(self, msg):
        self.updateSimulation()

    def behavior(self, xest, t):
        if t < 10:
            return self._cons
        else:
            return np.zeros(2)

def make_simulation():
    from RPFirmware.control.RPController import RPController
    from RPFirmware.control.RPEstimator import RPEstimator
    from RPFirmware.control.RPSystem import RPSystem
    from RPFirmware.control.RPSensors import RPSensors
    from RPFirmware.ResourcesManager import ResourcesManager

    rm = ResourcesManager()

    # COBYLA
    P = 7.51209586
    I = 1.97745718

    dt = 0.01
    ctrl = RPController(dt, P, I)
    sys = RPSystem()
    sensors = RPSensors()
    estimator = RPEstimator(dt)
    sim = RPSimulation(dt, ctrl, sys, sensors, estimator)

    c = rm.clk
    c.addObserver(sim, freq=100.)

    return sim
