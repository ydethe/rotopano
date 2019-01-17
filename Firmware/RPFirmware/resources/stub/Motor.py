import os

import numpy as np
from singleton3 import Singleton

from RPFirmware.resources.pi_settings import pan_motor, tilt_motor
from RPFirmware.Logger import logger


class Motor (object):
    def __init__(self, slp, m0, m1, m2, dir, stp, nstp, reduc, frac):
        self._slp  = slp
        self._m0   = m0
        self._m1   = m1
        self._m2   = m2
        self._dir  = dir
        self._stp  = stp
        self._nstp = nstp
        self._reduc = reduc

        self._den = 1

        self.activated = False
        self.angle = 0.
        
        self.setFracStep(frac)

        self.setSpeed(0)

    def activate(self):
        self.activated = True
        
    def deactivate(self):
        self.activated = False
        self.setSpeed(0)

    def isActivated(self):
        return self.activated

    def setFracStep(self, den):
        if den == 1:
            stg = [0,0,0]
        elif den == 2:
            stg = [1,0,0]
        elif den == 4:
            stg = [0,1,0]
        elif den == 8:
            stg = [1,1,0]
        elif den == 16:
            stg = [0,0,1]
        elif den == 32:
            stg = [1,0,1]
        else:
            raise ValueError

        self._den = den

    def getStep(self):
        stp = 2*np.pi/self._nstp/self._den
        return stp

    def getFracStep(self):
        return self._den

    def turn(self, angle, speed=2*np.pi/20):
        # n = 2**np.ceil(np.log2(np.abs(angle)/10.))
        # if n < 1:
        #     n = 1
        # if n > 32:
        #     n = 32
        # logger.debug("FracStep : %i" % n)
        # self.setFracStep(n)

        self.angle += angle
        
        if angle < 0:
            speed *= -1.
        wr = self.setSpeed(speed)
#         logger.debug("Vitesses : %f, %f\n" % (speed, wr))
        t = angle/wr
#         logger.debug("Temps tour : %f\n" % t)
        wr = self.setSpeed(0)

    def setFrequency(self, freq):
        return freq

    def setSpeed(self, w):
        # # Sécurité
        # if w > 2*np.pi/10.:
        #     w = 2*np.pi/10.
        # elif w < -2*np.pi/10.:
        #     w = -2*np.pi/10.

        freq = np.abs(w/(2*np.pi)*self._den*self._nstp/self._reduc)

        f_app = self.setFrequency(freq)
        w_app = 2*np.pi*f_app*self._reduc/(self._den*self._nstp)
        
        if w < 0:
            return -w_app
        else:
            return w_app



class PanMotor (Motor, metaclass=Singleton):
    def __init__(self):
        Motor.__init__(self, **pan_motor)

class TiltMotor (Motor, metaclass=Singleton):
    def __init__(self):
        Motor.__init__(self, **tilt_motor)
