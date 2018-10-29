<<<<<<< .mine
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

    def loop(self, pano_mode, pano_interval):
        cont = True
        self.counter.value += 1
        print(self.counter.value)
        time.sleep(pano_interval)
        if self.counter.value == 10:
            self.counter.value = 0
            cont = False
        return cont

    def getStateJSON(self):
        res  = {}

        st = self.getState()
        if st == BaseAction.STOPPED:
            res['state'] = 'STOPPED'
        elif st == BaseAction.RUNNING:
            res['state'] = 'RUNNING'
        elif st == BaseAction.PAUSED:
            res['state'] = 'PAUSED'

        res['avct'] = self.counter.value*10

        return res


if __name__ == '__main__':
    a = PanoramaAction()
    a.start(pano_mode="Photo", pano_interval=1.)
    =======
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
        print(self.counter.value)
        time.sleep(1)
        >>>>>>> .r61
