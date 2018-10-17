import time
from multiprocessing import Process, Value

from .Sensors import IMU
from .System import RPSystem
from SystemControl.Estimator import PassFilter
from .Controller import RPController
from SystemControl.Simulation import ASimulation


class RPInterface (ASimulation, Process):
   def __init__(self, dt, ctrl, sys, sensors, estimator):
      ASimulation.__init__(self, dt, ctrl, sys, sensors, estimator)
      self.setRealTime(True)
      self._cons_alt = Value('d',0.)
      self._cons_azi = Value('d',0.)
      Process.__init__(self, target=self._work, args=(self._cons_alt,self._cons_azi))
		
   def behavior(self, xest, t):
      return np.array([self._cons_alt.value, self._cons_azi.value])
      
   def setAltAz(self, alt, azi):
      self._cons_alt.value = alt
      self._cons_azi.value = azi
	
   def _work(self, alt, azi):
      while True:
         t0 = time.time()
         self.updateSimulation()
         while time.time()-t0 < self._dt:
            pass

def setup_interface():
   imu = IMU()
   sys = RPSystem()
   dt = 1./50.
   ctl = RPController()
   mf = PassFilter(['roll','pitch','yaw'])
   itf = RPInterface(dt, ctl,sys,imu,mf)
   
   itf.start()
   
   return itf
   
   