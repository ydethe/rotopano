import math

import numpy as np

from SystemControl.System import ASystem
from RPFirmware.ResourcesManager import ResourcesManager


def find_nearest(array,value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return array[idx-1]
    else:
        return array[idx]

class RPSystem (ASystem):
    def __init__(self):
        ASystem.__init__(self, name_of_states=['pan','tilt'])
        self.reset()
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

    def reset(self):
        self.setState(np.array([0.,0.]))

    @ASystem.updatemethod
    def update(self, t1 : float, t2 : float, u : np.array) -> None:
       u'''Integrates the system by one time step.
       Called at each simulation step.

       @param u \a array
          updateController vector. Dimension (p,1)

       @param dt (s) \a float
          Time step

       '''
       cmd_vpan,cmd_vtilt = u

       self.pan_motor.setSpeed(cmd_vpan)
       self.tilt_motor.setSpeed(cmd_vtilt)
