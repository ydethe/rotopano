import time

import numpy as np
import pigpio
from singleton3 import Singleton

from RPFirmware.Observe import Observable, Observer


class Clock (Observable, metaclass=Singleton):
    def __init__(self, freq):
        Observable.__init__(self)
        self.dt = 1./freq

        self.pi = pigpio.pi()

        self.CLK_PIN = 4
        self.pi.set_mode(self.CLK_PIN, pigpio.OUTPUT)
        istat = self.pi.hardware_clock(self.CLK_PIN, int(freq))

    def start(self):
        cb1 = self.pi.callback(self.CLK_PIN, pigpio.RISING_EDGE, self.notify)

    def notify(self, gpio, level, tick):
        for o in self.observers:
            o.handleMsg(None)
