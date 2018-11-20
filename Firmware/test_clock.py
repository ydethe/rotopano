import time

from RPFirmware.ResourcesManager import ResourcesManager
from RPFirmware.Observe import Observer
from RPFirmware.Logger import logger


class Visu (Observer):
    def __init__(self, name):
        self.name = name

    def setNbBeats(self, nbeats):
        self.nbeat = nbeats
        self.ibeat = 0

    def handleMsg(self, msg):
        self.ibeat += 1
        if self.ibeat == self.nbeat:
            self.ibeat = 0
            logger.debug(self.name)


if __name__ == '__main__':
    rm = ResourcesManager()
    v1 = Visu("v1")
    v2 = Visu("v2")
    c = rm.clk
    # c.addObserver(v1, freq=2.)
    c.addObserver(v2, freq=100.)
    c.start()
    logger.debug("Clock started")

    t0 = time.time()
    while time.time()-t0 < 15 or True:
        pass
