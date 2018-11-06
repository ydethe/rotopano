import time
import os

from RPFirmware.actions.BaseAction import BaseAction
from RPFirmware.Config import Config
from RPFirmware.resources.RPEphemeris import RPEphemeris
from RPFirmware.Logger import logger


class TrackingAction (BaseAction):
    @staticmethod
    def getName():
        return 'tracking'

    def __init__(self):
        BaseAction.__init__(self, name=self.getName())
        self.cfg = Config()

    def reset(self):
        self.kwargs['t_start'] = time.time()
        self.kwargs['alt'] = 0.
        self.kwargs['az'] = 0.
        self.kwargs['d'] = 0.
        if not 'trk_interval' in self.kwargs.keys():
            self.kwargs['trk_interval'] = 1.
        if not 'trk_duration' in self.kwargs.keys():
            self.kwargs['trk_duration'] = 10.

    def loop(self, kwargs):
        cont = True

        logger.debug("TrackingAction.loop : kwargs=%s\n" % str(kwargs))
        
        eph = RPEphemeris()
        alt, az, d = eph.getAltAz(name=kwargs['trk_body'], lat=kwargs['lat'], lon=kwargs['lon'], height=0)
        kwargs['alt'] = alt
        kwargs['az'] = az
        kwargs['d'] = d

        time.sleep(kwargs['trk_interval'])

        if time.time() > kwargs['t_start'] + kwargs['trk_duration']:
            cont = False

        return cont

