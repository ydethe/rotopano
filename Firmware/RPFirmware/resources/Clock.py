import time

import numpy as np
import pigpio
from singleton3 import Singleton

from RPFirmware.Observe import Observable, Observer


class Clock (Observable, metaclass=Singleton):
    def __init__(self, freq, clk_pin=4, pi=None):
        Observable.__init__(self)
        self.dt = 1./freq
        self._freq = freq

        if pi is None:
            self.pi = pigpio.pi()
        else:
            self.pi = pi

        self.clk_pin = clk_pin
        self.pi.set_mode(self.clk_pin, pigpio.OUTPUT)
        istat = self.pi.hardware_clock(self.clk_pin, int(freq))
        self.pi.wave_add_generic([
           pigpio.pulse(0, 1<<self.clk_pin, int(self.dt/2)),
           pigpio.pulse(1<<self.clk_pin, 0, int(self.dt/2)),
           ])
        self.wid = self.pi.wave_create()

    def addObserver(self, obs, freq=None):
        Observable.addObserver(self,obs)
        if freq is None:
            nbeats = 1
        else:
            nbeats = int(self._freq/freq)

        obs.setNbBeats(nbeats)

    def getFrequency(self):
        return self._freq

    def start(self):
        self.pi.wave_send_using_mode(self.wid, pigpio.WAVE_MODE_REPEAT_SYNC)
        while self.pi.wave_tx_at() != self.wid:
            pass

        cb1 = self.pi.callback(self.clk_pin, pigpio.RISING_EDGE, self.notify)

    def __del__(self):
        self.pi.wave_tx_stop()
        self.pi.wave_delete(self.wid)

    def notify(self, gpio, level, tick):
        for o in self.observers:
            o.handleMsg(None)
