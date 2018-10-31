import time

from RPFirmware.actions.BaseAction import BaseAction
from RPFirmware.Config import Config


class PanoramaAction (BaseAction):
    @staticmethod
    def getName():
        return 'panorama'

    def __init__(self):
        BaseAction.__init__(self, name=self.getName())
        self.cfg = Config()

    def reset(self):
        self.kwargs['counter'] = 0
        self.kwargs['avct'] = 0
        if not 'pano_interval' in self.kwargs.keys():
            self.kwargs['pano_interval'] = 1.

    def loop(self, kwargs):
        cont = True

        fic = open('/home/ydethe/mysite/RPFirmware/debug.log','a')
        fic.write("PanoramaAction.loop : kwargs=%s\n" % str(kwargs))
        fic.close()

        kwargs['counter'] += 1
        kwargs['avct'] = kwargs['counter']*10

        time.sleep(kwargs['pano_interval'])

        if kwargs['counter'] == 10:
            cont = False
            kwargs['counter'] = 0
            kwargs['avct'] = 0

        return cont
