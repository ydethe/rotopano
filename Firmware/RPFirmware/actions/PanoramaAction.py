import time
import os

import numpy as np

from RPFirmware.actions.BaseAction import BaseAction
from RPFirmware.Config import Config
from RPFirmware.ResourcesManager import ResourcesManager
from RPFirmware.Logger import logger


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
        self.kwargs['sit_counter'] = 0
        self.kwargs['gis_counter'] = 0
        self.kwargs['avct'] = 0
        sv = self.cfg.getParam('sensor_vsize_mm')
        sh = self.cfg.getParam('sensor_hsize_mm')
        f = self.cfg.getParam('focal_length_mm')
        overlap = self.cfg.getParam('overlap_p100')

        gis_stp0 = 2*np.arctan(sv/(2*f))*(1 - overlap/100)
        self.kwargs['gis_step'] = gis_stp0
        self.kwargs['nb_gis_step'] = int(np.ceil(2*np.pi/gis_stp0))

        sit_stp0 = 2*np.arctan(sh/(2*f))*(1 - overlap/100)
        self.kwargs['sit_step'] = sit_stp0
        self.kwargs['nb_gis_step'] = int(np.ceil(np.pi/2./gis_stp0))

        if not 'pano_interval' in self.kwargs.keys():
            self.kwargs['pano_interval'] = 1.

    def loop(self, kwargs):
        cont = True

        logger.debug("PanoramaAction.loop : kwargs=%s\n" % str(kwargs))

        if kwargs['pano_mode'] == 'Photo':
            cont = False
            kwargs['counter'] = 0
            kwargs['avct'] = 0
            self.kwargs['nb_step'] = 1

            self.rm.pan.activate()
            self.rm.tilt.activate()
            apn_path = self.apn.takePicture()
            self.rm.pan.deactivate()
            self.rm.tilt.deactivate()
            self.apn.downloadPicture(apn_path, 'pics/photo_%i.jpg' % kwargs['counter'])

        elif kwargs['pano_mode'] == 'Horizontal panorama':
            kwargs['gis_counter'] += 1

            kwargs['avct'] = int(kwargs['gis_counter']/self.kwargs['nb_step']*100)

            self.rm.pan.activate()
            self.rm.tilt.activate()
            self.rm.pan.turn(self.kwargs['step'], speed=2*np.pi/10.)
            apn_path = self.apn.takePicture()
            self.apn.downloadPicture(apn_path, 'pics/photo_%i.jpg' % kwargs['gis_counter'])

            time.sleep(kwargs['pano_interval'])

            if kwargs['gis_counter'] == self.kwargs['nb_step']:
                cont = False
                kwargs['gis_counter'] = 0
                kwargs['avct'] = 0
                self.rm.pan.deactivate()
                self.rm.tilt.deactivate()

        # elif kwargs['pano_mode'] == 'Half sphere panorama':
        #     kwargs['counter'] += 1
        #
        #     kwargs['avct'] = int(kwargs['gis_counter']/self.kwargs['nb_gis_step']*kwargs['sit_counter']/self.kwargs['nb_sit_step']*100)
        #
        #     self.rm.pan.activate()
        #     self.rm.pan.turn(self.kwargs['step'], speed=2*np.pi/10.)
        #     apn_path = self.apn.takePicture()
        #     self.apn.downloadPicture(apn_path, 'pics/photo_%i.jpg' % kwargs['counter'])
        #
        #     time.sleep(kwargs['pano_interval'])
        #
        #     if kwargs['gis_counter'] == self.kwargs['nb_gis_step'] and kwargs['sit_counter'] == self.kwargs['nb_sit_step']:
        #         cont = False
        #         kwargs['gis_counter'] = 0
        #         kwargs['sit_counter'] = 0
        #         kwargs['avct'] = 0
        #         self.rm.pan.deactivate()

        return cont
