import time

import numpy as np

from SystemControl.Simulation import ASimulation
from RPFirmware.Observe import Observer
from RPFirmware.Logger import logger


class RPSimulation (ASimulation, Observer):
    def __init__(self, ctrl, sys, sensors, estimator):
        ASimulation.__init__(self, ctrl, sys, sensors, estimator)
        self._cons = np.zeros(2)
        self._tprec = None

    def setNbBeats(self, nbeats):
        self.nbeat = nbeats
        self.ibeat = 0

    def setConsigne(self, cons):
        self._cons = cons

    def handleMsg(self, msg):
        self.ibeat += 1
        if self.ibeat == self.nbeat:
            self.ibeat = 0
            if self._tprec is None:
                self._tprec = time.time()
            else:
                t = time.time()
                self.updateSimulation(self._tprec, t)
                self._tprec = t
                u = self._log.getValue('cmd_vtilt')
                logger.debug('t,u :\t%f,%f' % (time.time(),u[-1]))

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

    ctrl = RPController(P, I)
    sys = RPSystem()
    sensors = RPSensors()
    estimator = RPEstimator()
    sim = RPSimulation(ctrl, sys, sensors, estimator)

    c = rm.clk
    c.addObserver(sim, freq=100.)

    return sim
