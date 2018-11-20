import time

from RPFirmware.ResourcesManager import ResourcesManager
from RPFirmware.Observe import Observer
from RPFirmware.Logger import logger


class Visu (Observer):
    def __init__(self, nbeat):
        self.nbeat = nbeat
        self.ibeat = 0

    def handleMsg(self, msg):
        self.ibeat += 1
        if self.ibeat == self.nbeat:
            self.ibeat = 0
            logger.debug("Visu : %i" % (self.nbeat,))


if __name__ == '__main__':
    rm = ResourcesManager()
    v1 = Visu(2500)
    v2 = Visu(5000)
    c = rm.clk
    c.addObserver(v1)
    c.addObserver(v2)
    logger.debug("Clock started")
    c.start()

    t0 = time.time()
    while time.time()-t0 < 10:
        pass
