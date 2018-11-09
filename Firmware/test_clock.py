from RPFirmware.Clock import Clock
from RPFirmware.Observe import Observer

        
class Visu (Observer):
    def __init__(self, nbeat):
        self.nbeat = nbeat
        
    def handleMsg(self, msg):
        print("Visu : ", self.nbeat, time.time(), msg)
        
        
if __name__ == '__main__':
    v1 = Visu(2500)
    v2 = Visu(5000)
    c = Clock(5000)
    c.addObserver(v1)
    c.addObserver(v2)
    c.start()
    
    