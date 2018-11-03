import time

import numpy as np
from singleton3 import Singleton

import pigpio

from RPFirmware.pi_settings import pan_motor, tilt_motor
from RPFirmware.Logger import Logger


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
        
    def activate(self):
        self.pi.write(self._slp, 0)
        
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
    
    def getFracStep(self):
        return self._den
        
    def turn(self, angle, speed=2*np.pi/20):
        if angle < 0:
            speed *= -1.
        wr = self.setSpeed(speed)
        Logger().log("Vitesses : %f, %f\n" % (speed, wr))
        t = angle/wr
        Logger().log("Temps tour : %f\n" % t)
        time.sleep(t)
        wr = self.setSpeed(0)
        
    def setSpeed(self, w):
        freq = np.int(np.abs(w/(2*np.pi)*self._den*self._nstp/self._reduc))
        
        if w < 0.:
            self.pi.write(self._dir, 0)
        else:
            self.pi.write(self._dir, 1)
        
        if w == 0:
            self.pi.set_PWM_dutycycle(self._stp, 0)
            fapp = 0
        else:
            self.pi.set_PWM_dutycycle(self._stp, 255/2)
            fapp = self.pi.set_PWM_frequency(self._stp, freq)
        
        if fapp == pigpio.PI_BAD_USER_GPIO:
            raise ArgumentError("PI_BAD_USER_GPIO")
        elif fapp == pigpio.PI_NOT_PERMITTED:
            raise ArgumentError("PI_NOT_PERMITTED")
        else:
            if w < 0.:
                return -fapp*2*np.pi/(self._den*self._nstp)*self._reduc
            else:
                return fapp*2*np.pi/(self._den*self._nstp)*self._reduc
                
                
class PanMotor (Motor, metaclass=Singleton):
    def __init__(self):
        Motor.__init__(self, **pan_motor)
        
class TiltMotor (Motor, metaclass=Singleton):
    def __init__(self):
        Motor.__init__(self, **tilt_motor)
        
        
        