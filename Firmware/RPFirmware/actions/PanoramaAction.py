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

    def loop(self):
        self.counter.value += 1
        time.sleep(1)
        