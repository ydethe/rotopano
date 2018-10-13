from libSystemControl.Simulation import ASimulation
from multiprocessing import Process, Value


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
         self.updateSimulation()
			
