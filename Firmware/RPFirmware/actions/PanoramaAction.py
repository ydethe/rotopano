import time
from multiprocessing import Value

from RPFirmware.actions.BaseAction import BaseAction
from RPFirmware.Config import Config


class PanoramaAction (BaseAction):
    @staticmethod
    def getName():
        return 'panorama'

    def __init__(self):
        self.cfg = Config()
        self.counter = Value('i',0)
        BaseAction.__init__(self, name='panorama')
        self.kwargs['pano_mode'] = 'Photo'
        self.kwargs['pano_interval'] = 1.
        
    def reset(self, **kwargs):
        self.counter.value = 0
        
    def loop(self):
        cont = True
        self.counter.value += 1
        print("counter", self.counter.value, flush=True)
        print("pano_interval", self.kwargs['pano_interval'], flush=True)
        time.sleep(self.kwargs['pano_interval'])
        if self.counter.value == 10:
            cont = False
        return cont

    def getState(self):
        res  = BaseAction.getState(self)

        res['avct'] = self.counter.value*10

        return res


if __name__ == '__main__':
    a = PanoramaAction()
    a.start(pano_mode="Photo", pano_interval=1.)
    