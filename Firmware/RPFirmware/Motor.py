import numpy as np

import pigpio


class Motor (object):
    def __init__(self, slp, m0, m1, m2, dir, stp, nstp):
        self._slp  = slp 
        self._m0   = m0  
        self._m1   = m1  
        self._m2   = m2  
        self._dir  = dir 
        self._stp  = stp 
        self._nstp = nstp
        
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
    
    def getFracStep(self):
        return self._den
        
    def setSpeed(self, w):
        freq = np.int(np.abs(w/(2*np.pi)*self._den*self._nstp))
        
        if w < 0.:
            self.pi.write(self._dir, 0)
        else:
            self.pi.write(self._dir, 1)
        
        self.pi.set_PWM_dutycycle(self._stp, 255/2)
        fapp = self.pi.set_PWM_frequency(self._stp, freq)
        if fapp == pigpio.PI_BAD_USER_GPIO:
            raise ArgumentError("PI_BAD_USER_GPIO")
        elif fapp == pigpio.PI_NOT_PERMITTED:
            raise ArgumentError("PI_NOT_PERMITTED")
        else:
            if w < 0.:
                return -fapp*2*np.pi/(self._den*self._nstp)
            else:
                return fapp*2*np.pi/(self._den*self._nstp)
                