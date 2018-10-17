from multiprocessing import Process, Value
import time


class Tache (Process):
   def __init__(self):
      self.tmp = Value('d',1.)
      Process.__init__(self, target=self._work, args=(self.tmp,))
      
   def setTempo(self, dt):
      self.tmp.value = dt
      
   def getTempo(self):
      return self.tmp.value
      
   def _work(self, t):
      while True:
         t0 = time.time()
         
         print(t.value)
         
         while time.time()-t0 < t.value:
            pass
            
            
            