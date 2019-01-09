import time

import numpy as np
from singleton3 import Singleton

import pigpio

from RPFirmware.resources.pi_settings import pan_motor, tilt_motor
from RPFirmware.Logger import logger


class Motor (object):
    def __init__(self, slp, m0, m1, m2, dir, stp, nstp, reduc):
        self._slp  = slp
        self._m0   = m0
        self._m1   = m1
        self._m2   = m2
        self._dir  = dir
        self._stp  = stp
        self._nstp = nstp
        self._reduc = reduc

        self._den = 1

        self.pi = pigpio.pi()
        if not self.pi.connected:
            raise SystemError("pigpio not connected")

        self.pi.set_mode(self._slp , pigpio.OUTPUT)
        self.pi.set_mode(self._m0  , pigpio.OUTPUT)
        self.pi.set_mode(self._m1  , pigpio.OUTPUT)
        self.pi.set_mode(self._m2  , pigpio.OUTPUT)
        self.pi.set_mode(self._dir , pigpio.OUTPUT)
        self.pi.set_mode(self._stp , pigpio.OUTPUT)

        self.pi.write(self._slp , 0)
        self.pi.write(self._m0  , 0)
        self.pi.write(self._m1  , 0)
        self.pi.write(self._m2  , 0)
        self.pi.write(self._dir , 0)
        self.pi.write(self._stp , 0)

        self.old_wid = None

    def activate(self):
        self.pi.write(self._slp, 1)

    def deactivate(self):
        self.pi.write(self._slp, 0)

    def isActivated(self):
        return (self.pi.read(self._slp) == 1)

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

        self.pi.write(self._m0, stg[0])
        self.pi.write(self._m1, stg[1])
        self.pi.write(self._m2, stg[2])

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

        if angle < 0:
            speed *= -1.
        wr = self.setSpeed(speed)
#         logger.debug("Vitesses : %f, %f\n" % (speed, wr))
        t = angle/wr
#         logger.debug("Temps tour : %f\n" % t)
        time.sleep(t)
        wr = self.setSpeed(0)

    def setSpeed(self, w):
        # # Sécurité
        # if w > 2*np.pi/10.:
        #     w = 2*np.pi/10.
        # elif w < -2*np.pi/10.:
        #     w = -2*np.pi/10.

        freq = np.int(np.abs(w/(2*np.pi)*self._den*self._nstp/self._reduc))

        if w < 0.:
            self.pi.write(self._dir, 1)
        else:
            self.pi.write(self._dir, 0)

        if w == 0:
            self.pi.wave_tx_stop()

            if self.old_wid is not None:
               self.pi.wave_delete(self.old_wid)

        else:
            micros = int(1e6/freq)
            self.pi.wave_add_generic([
               pigpio.pulse(1<<self._stp,    0, micros//2),
               pigpio.pulse(   0, 1<<self._stp, micros//2),
               ])

            new_wid = self.pi.wave_create()

            if self.old_wid is not None:
               self.pi.wave_send_using_mode(
                  new_wid, pigpio.WAVE_MODE_REPEAT_SYNC)

               # Spin until the new wave has started.
               while self.pi.wave_tx_at() != new_wid:
                  pass

               # It is then safe to delete the old wave.
               self.pi.wave_delete(self.old_wid)

            else:
               self.pi.wave_send_repeat(new_wid)

            self.old_wid = new_wid

        return w


class PanMotor (Motor, metaclass=Singleton):
    def __init__(self):
        Motor.__init__(self, **pan_motor)

class TiltMotor (Motor, metaclass=Singleton):
    def __init__(self):
        Motor.__init__(self, **tilt_motor)


m = PanMotor()
m.activate()
m.setFracStep(16)
m.turn(2*np.pi, speed=2*np.pi/1)
m.turn(-2*np.pi, speed=2*np.pi/1)
m.deactivate()
