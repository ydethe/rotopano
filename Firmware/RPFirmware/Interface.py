from libSystemControl.Simulation import ASimulation


class RPInterface (ASimulation):
   def __init__(self, dt, ctrl, sys, sensors, estimator):
      ASimulation.__init__(self, dt, ctrl, sys, sensors, estimator)
      self.setRealTime(True)
   
   def behavior(self, xest, t):
      return np.zeros(2)
      
      