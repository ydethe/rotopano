import time

from RPFirmware.actions.BaseAction import BaseAction
from RPFirmware.Config import Config


class PanoramaAction (BaseAction):
    @staticmethod
    def getName():
        return 'panorama'

    def __init__(self):
        BaseAction.__init__(self, name='panorama')
        self.cfg = Config()
        self.kwargs['counter'] = 0

    def reset(self):
        self.kwargs['counter'] = 0

    def loop(self, kwargs):
        cont = True
        self.kwargs['counter'] += 1
        time.sleep(kwargs['pano_interval'])
        if self.kwargs['counter'] == 10:
            cont = False
        return cont

    def getState(self):
        res  = BaseAction.getState(self)

        res['avct'] = self.kwargs['counter']*10

        return res


if __name__ == '__main__':
    a = PanoramaAction()
    a.start(pano_mode="Photo", pano_interval=1.)
