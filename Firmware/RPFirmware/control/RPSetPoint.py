import numpy as np

from SystemControl.SetPoint import ASetPoint


class RPSetPoint (ASetPoint):
   def __init__(self):
      u'''Class initialisation

      '''
      ASetPoint.__init__(self, 'spt', ['cons_pan','cons_tilt'])

   @ASetPoint.updatemethod
   def update(self, t1 : float, t2 : float, inputs : dict) -> None:
      self.setState(np.zeros(2))
