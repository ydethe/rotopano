import time
from multiprocessing import Value

from.BaseAction import BaseAction
from ..Config import Config


class PanoramaAction (BaseAction):
    @staticmethod
    def getName():
        return 'panorama'

    def __init__(self):
        BaseAction.__init__(self, name='panorama')
        self.cfg = Config()
        self.counter = Value('i',0)

    def _work(self):
        for i in range(20):
            if self.getState() == BaseAction.RUNNING:
               pass
            elif self.getState() == BaseAction.PAUSED:
               while self.getState() == BaseAction.PAUSED:
                   pass
            elif self.getState() == BaseAction.STOPPED:
               break
            self.counter.value = i
            time.sleep(1)
        