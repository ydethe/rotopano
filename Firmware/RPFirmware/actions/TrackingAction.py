import time

from RPFirmware.actions.BaseAction import BaseAction
from RPFirmware.Config import Config
from RPFirmware.RPEphemeris import RPEphemeris


class TrackingAction (BaseAction):
    @staticmethod
    def getName():
        return 'tracking'

    def __init__(self):
        BaseAction.__init__(self, name='tracking')
        self.cfg = Config()
        self.reset()

    def reset(self):
        self.kwargs['t_start'] = time.time()
        self.kwargs['alt'] = 0.
        self.kwargs['az'] = 0.
        self.kwargs['d'] = 0.
        self.kwargs['lat'] = 0.
        self.kwargs['lon'] = 0.

    def loop(self):
        cont = True

        eph = RPEphemeris()
        bdy = eph.getBody(self.kwargs['trk_body'])
        alt, az, d = eph.getAltAz(bdy, lat=self.kwargs['lat'], lon=self.kwargs['lon'], height=0)
        self.kwargs['alt'] = alt
        self.kwargs['az'] = az
        self.kwargs['d'] = d

        time.sleep(self.kwargs['trk_interval'])

        if time.time() > self.kwargs['t_start'] + self.kwargs['trk_duration']:
            cont = False

        return cont
