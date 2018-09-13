import unittest
import time

import numpy as np

from libSystemControl.Simulation import ASimulation
from libSystemControl.Controller import NullController
from libSystemControl.System import ASystem
from RPFirmware.Sensors import IMU
from libSystemControl.Estimator import MadgwickFilter, MahonyFilter


class TSimulation (ASimulation):
   def behavior(self, x, t):
      return np.array([0.])

class TSystem (ASystem):
   def __init__(self):
      ASystem.__init__(self, ['x'], method='vode')
      
   def behavior(self, x, u, t):
      return np.zeros(1)

class TestIMU (unittest.TestCase):
    def test_imu(self):
        dt = 2e-3
        imu = IMU()
        est = MahonyFilter(dt)
        ctrl = NullController(['cmd'])
        sys = TSystem()
        sys.setState(np.array([0.]), 0.)

        tfin = 5.
        t0 = time.time()
        sim = TSimulation(dt, ctrl, sys, imu, est)
        sim.simulate(tfin)
        t1 = time.time()

        log = sim.getLogger()

        pitch = log.getValue('pitch*180/np.pi')
        n = len(pitch)

        print("Freq %.1fHz" % (n/(t1-t0)))
        print(pitch)
        

   
if __name__ == '__main__':
   unittest.main()
   
   
   
