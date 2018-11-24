import time

import numpy as np

from SystemControl.Simulation import Simulation
from RPFirmware.Observe import Observer
from RPFirmware.Logger import logger


class RPSimulation (Simulation, Observer):
    def __init__(self, ctrl, sys, sensors, estimator):
        Simulation.__init__(self)
        Observer.__init__(self)
        self.setElements([ctrl, sys, sensors, sensors])
        self._cons = np.zeros(2)
        self._tprec = None

    def setNbBeats(self, nbeats):
        self.nbeat = nbeats
        self.ibeat = 0

    def handleMsg(self, msg):
        self.ibeat += 1
        if self.ibeat == self.nbeat:
            self.ibeat = 0
            if self._tprec is None:
                self._tprec = time.time()
            else:
                t = time.time()
                self.update(self._tprec, t)
                self._tprec = t
                tilt_mes = self._log.getValue('tilt_mes')
                # logger.debug('t,tilt_mes :\t%f,%fdeg' % (time.time(),180/np.pi*tilt_mes[-1]))


def make_simulation():
    from RPFirmware.control.RPController import RPController
    from RPFirmware.control.RPEstimator import RPEstimator
    from RPFirmware.control.RPSystem import RPSystem
    from RPFirmware.control.RPSensors import RPSensors
    from RPFirmware.control.RPSetPoint import RPSetPoint
    from RPFirmware.ResourcesManager import ResourcesManager

    rm = ResourcesManager()

    # COBYLA
    P = 7.51209586
    I = 1.97745718
    # P = 0.
    # I = 0.

    # user = RPSetPoint(np.ones(2)*10*np.pi/180.)
    user = RPSetPoint(np.zeros(2))
    ctrl = RPController(P, I, user)
    sys = RPSystem()
    sensors = RPSensors()
    estimator = RPEstimator(ctrl)
    sim = RPSimulation(ctrl, sys, sensors, estimator)

    log = sim.getLogger()
    log.setFile('simu.log')

    c = rm.clk
    c.addObserver(sim, freq=100.)

    return sim
