import time
import os

import numpy as np

from RPFirmware.actions.BaseAction import BaseAction
from RPFirmware.Config import Config
from RPFirmware.ResourcesManager import ResourcesManager


class PanoramaAction (BaseAction):
    @staticmethod
    def getName():
        return 'panorama'

    def __init__(self):
        self.cfg = Config()
        self.rm = ResourcesManager()
        self.apn = self.rm.apn
        BaseAction.__init__(self, name=self.getName())
        self.reset()
        
    def reset(self):
        self.apn.connect()
        self.kwargs['counter'] = 0
        self.kwargs['avct'] = 0
        d = self.cfg.getParam('sensor_hsize_mm')
        f = self.cfg.getParam('focal_length_mm')
        overlap = self.cfg.getParam('overlap_p100')
        
        stp0 = 2*np.arctan(d/(2*f))*(1 - overlap/100)
        self.kwargs['step'] = stp0
        self.kwargs['nb_step'] = int(np.ceil(2*np.pi/stp0))
        
        if not 'pano_interval' in self.kwargs.keys():
            self.kwargs['pano_interval'] = 1.
        
        self.rm.pan.activate()
        
    def loop(self, kwargs):
        cont = True

        self.rm.log.debug("PanoramaAction.loop : kwargs=%s\n" % str(kwargs))
        
        kwargs['counter'] += 1
        kwargs['avct'] = int(kwargs['counter']/self.kwargs['nb_step']*100)

        self.rm.pan.turn(self.kwargs['step'], speed=2*np.pi/10.)
        apn_path = self.apn.takePicture()
        self.apn.downloadPicture(apn_path, 'pics/photo_%i.jpg' % kwargs['counter'])
        
        time.sleep(kwargs['pano_interval'])

        if kwargs['counter'] == self.kwargs['nb_step']:
            cont = False
            kwargs['counter'] = 0
            kwargs['avct'] = 0
            self.rm.pan.deactivate()

        return cont
        
        
        