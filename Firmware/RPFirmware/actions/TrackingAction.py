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

    def reset(self, kwargs):
        fic = open('/home/ydethe/mysite/RPFirmware/debug.log','a')
        fic.write("TrackingAction : reset\n")
        fic.close()

        kwargs['t_start'] = time.time()
        kwargs['alt'] = 0.
        kwargs['az'] = 0.
        kwargs['d'] = 0.
        kwargs['lat'] = 0.
        kwargs['lon'] = 0.

    def loop(self, kwargs):
        cont = True

        fic = open('/home/ydethe/mysite/RPFirmware/debug.log','a')
        fic.write("TrackingAction.loop : kwargs=%s\n" % str(kwargs))
        fic.close()

        eph = RPEphemeris()
        bdy = eph.getBody(kwargs['trk_body'])
        alt, az, d = eph.getAltAz(bdy, lat=kwargs['lat'], lon=kwargs['lon'], height=0)
        kwargs['alt'] = alt
        kwargs['az'] = az
        kwargs['d'] = d

        time.sleep(kwargs['trk_interval'])

        if time.time() > kwargs['t_start'] + kwargs['trk_duration']:
            cont = False

        return cont
