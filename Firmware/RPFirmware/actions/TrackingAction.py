import time
import os

from RPFirmware.actions.BaseAction import BaseAction
from RPFirmware.Config import Config
from RPFirmware.ResourcesManager import ResourcesManager
from RPFirmware.Logger import logger


class TrackingAction (BaseAction):
    @staticmethod
    def getName():
        return 'tracking'

    def __init__(self):
        self.cfg = Config()
        self.rm = ResourcesManager()
        BaseAction.__init__(self, name=self.getName())
        self.reset()
        
    def reset(self):
        self.kwargs['t_start'] = time.time()
        
        self.kwargs['alt'] = 0.
        self.kwargs['az'] = 0.
        self.kwargs['d'] = 0.
        
        self.kwargs['lat'] = 0.
        self.kwargs['lon'] = 0.
        self.kwargs['alt'] = 0.
        
        if not 'trk_interval' in self.kwargs.keys():
            self.kwargs['trk_interval'] = 1.
        if not 'trk_duration' in self.kwargs.keys():
            self.kwargs['trk_duration'] = 10.

    def loop(self, kwargs):
        cont = True

        logger.debug("TrackingAction.loop : kwargs=%s\n" % str(kwargs))
        
        tps,lat,lon,alt = ResourcesManager().gps.getTpsLatLonAlt()
        logger.debug("TrackingAction.loop : GPS=%f,%f,%f\n" % (lat,lon,alt))
        
        alt, az, d = ResourcesManager().eph.getAltAz(name=kwargs['trk_body'], lat=lat, lon=lon, height=alt)
        kwargs['alt'] = alt
        kwargs['az'] = az
        kwargs['d'] = d
        kwargs['lat'] = lat
        kwargs['lon'] = lon
        kwargs['alt'] = alt
        
        time.sleep(kwargs['trk_interval'])

        if time.time() > kwargs['t_start'] + kwargs['trk_duration']:
            cont = False

        return cont

