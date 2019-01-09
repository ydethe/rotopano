import math

import numpy as np

from SystemControl.System import ASystem
from RPFirmware.ResourcesManager import ResourcesManager


class RPSystem (ASystem):
    def __init__(self):
        ASystem.__init__(self, 'sys', name_of_states=['pan','tilt'])
        self.lfreq = np.array([10, 20, 40, 50, 80, 100, 160, 200, 250, 320, 400, 500, 800, 1000, 1600, 2000, 4000, 8000])
        self.den = 8
        self.nstp = 200
        self.reduc = 0.75
        self.stp = 2*np.pi/(self.nstp*self.den)
        self.aov = 2*np.arctan(15.6/(2*200))
        self.lim_cmd = self.lfreq[0]*2*np.pi/(self.den*self.nstp)*self.reduc
        self.prec = self.aov / 10.

        self.pan_motor = ResourcesManager().pan
        self.tilt_motor = ResourcesManager().tilt

    def transition(self, t, x, u):
        pass

    @ASystem.updatemethod
    # @profile
    def update(self, t1 : float, t2 : float, inputs : dict) -> None:
       u'''Integrates the system by one time step.
       Called at each simulation step.

       @param u \a array
          updateController vector. Dimension (p,1)

       @param dt (s) \a float
          Time step

       '''
       u = self.getStateForInput(inputs, 'command')
       cmd_vpan,cmd_vtilt = u

       self.pan_motor.setSpeed(cmd_vpan)
       self.tilt_motor.setSpeed(cmd_vtilt)
