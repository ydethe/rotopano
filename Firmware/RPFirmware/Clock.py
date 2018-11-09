import time
from math import gcd

import numpy as np
import pigpio

from RPFirmware.Observe import Observable, Observer


def pgcd(*n):
    """Calcul du 'Plus Grand Commun Diviseur' de n (>=2) valeurs entières (Euclide)"""
    if len(n) == 1:
        return 1
        
    p = gcd(n[0], n[1])
    for x in n[2:]:
        p = gcd(p, x)
    return p
    
class Clock (Observable):
    def __init__(self, freq):
        Observable.__init__(self)
        self.dt = 1./freq
        self.icount = 0
        self.ncount = 0
        
        self.pi = pigpio.pi()

        self.CLK_PIN = 4        
        self.pi.set_mode(self.CLK_PIN, pigpio.OUTPUT)
        istat = self.pi.hardware_clock(self.CLK_PIN, int(freq))
        
    def start(self):
        lbeat = [x.nbeat for x in self.observers]
        self.ncount = np.prod(lbeat)/pgcd(*lbeat)
        cb1 = self.pi.callback(self.CLK_PIN, pigpio.RISING_EDGE, self.notify)

    def notify(self, gpio, level, tick):
        for o in self.observers:
            if self.icount % o.nbeat == 0:
                o.handleMsg(msg)
        if self.icount == self.ncount:
            self.icount = 0
        
        
class Visu (Observer):
    def __init__(self, nbeat):
        self.nbeat = nbeat
        
    def handleMsg(self, msg):
        print("Visu : ", self.nbeat, time.time(), msg)
        
        
if __name__ == '__main__':
    v1 = Visu(5)
    v2 = Visu(6)
    c = Clock(30)
    c.addObserver(v1)
    c.addObserver(v2)
    c.start()
    
    