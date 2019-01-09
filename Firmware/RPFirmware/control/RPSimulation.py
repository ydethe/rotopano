import time

import numpy as np

from SystemControl.Simulation import Simulation
from RPFirmware.ResourcesManager import ResourcesManager
from RPFirmware.Observe import Observer
from RPFirmware.Logger import logger
from RPFirmware.control.RPController import RPController, RPBangBangController
from RPFirmware.control.RPEstimator import RPAngleEstimator, RPAngleBiasEstimator
from RPFirmware.control.RPSystem import RPSystem
from RPFirmware.control.RPSensors import RPSensors
from RPFirmware.control.RPSetPoint import RPSetPoint


class RPSimulation (Simulation, Observer):
    def __init__(self):
        Simulation.__init__(self)
        Observer.__init__(self)

        self.fmax = 8000
        self.den = 16
        self.nstp = 200
        self.reduc = 0.75
        self.stp = 2*np.pi/(self.nstp*self.den)
        self.aov = 2*np.arctan(15.6/(2*200))
        self.lim_cmd = self.fmax*2*np.pi/(self.den*self.nstp)*self.reduc
        self.prec = self.aov/10.

        self.user = RPSetPoint()
        # self.ctrl = RPController(7.6, 0.)
        self.ctrl = RPBangBangController(self.prec, self.lim_cmd)
        self.sys  = RPSystem()
        self.cpt  = RPSensors()
        self.kal  = RPAngleEstimator()

        self.addElement(self.user)
        self.addElement(self.ctrl)
        self.addElement(self.sys)
        self.addElement(self.cpt)
        self.addElement(self.kal)

        self.linkElements(self.user, self.ctrl, 'setpoint')
        self.linkElements(self.ctrl, self.sys,  'command')
        self.linkElements(self.cpt,  self.kal,  'measurement')
        self.linkElements(self.ctrl, self.kal,  'command')
        self.linkElements(self.kal,  self.ctrl, 'estimation')

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
    rm = ResourcesManager()
    sim = RPSimulation()

    log = sim.getLogger()
    log.setOutputLoggerFile('simu.log')

    c = rm.clk
    c.addObserver(sim, freq=100.)

    return sim
