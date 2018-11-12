import time

from RPFirmware.ResourcesManager import ResourcesManager
from RPFirmware.Observe import Observer

        
class Visu (Observer):
    def __init__(self, nbeat):
        self.nbeat = nbeat
        self.ibeat = 0
        
    def handleMsg(self, msg):
        self.ibeat += 1
        if self.ibeat == self.nbeat:
            self.ibeat = 0
            print("Visu : ", self.nbeat, time.time(), flush=True)
        
        
if __name__ == '__main__':
    rm = ResourcesManager()
    v1 = Visu(2500)
    v2 = Visu(5000)
    c = rm.clk
    c.addObserver(v1)
    c.addObserver(v2)
    c.start()
    
    while True:
        pass
        
        