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
        self.kwargs['sit_counter'] = 1
        self.kwargs['gis_counter'] = 1
        self.kwargs['avct'] = 0
        sv = self.cfg.getParam('sensor_vsize_mm')
        sh = self.cfg.getParam('sensor_hsize_mm')
        f = self.cfg.getParam('focal_length_mm')
        overlap = self.cfg.getParam('overlap_p100')

        self.kwargs['ouv_horz'] = 2*np.arctan(sh/(2*f))
        gis_stp0 = self.kwargs['ouv_horz']*(1 - overlap/100)
        self.kwargs['gis_step0'] = gis_stp0
        self.kwargs['gis_step'] = gis_stp0
        self.kwargs['nb_gis_step'] = int(np.ceil(2*np.pi/gis_stp0))

        sit_stp0 = 2*np.arctan(sv/(2*f))*(1 - overlap/100)
        self.kwargs['sit_step'] = sit_stp0
        self.kwargs['nb_sit_step'] = int(np.ceil(np.pi/2./sit_stp0))

        if not 'pano_interval' in self.kwargs.keys():
            self.kwargs['pano_interval'] = 1.

    def loop(self, kwargs):
        logger.debug("PanoramaAction.loop : kwargs=%s\n" % str(kwargs))

        if kwargs['pano_mode'] == 'Photo':
            kwargs['avct'] = 0

            self.rm.pan.activate()
            self.rm.tilt.activate()
            apn_path = self.apn.takePicture('pics/photo_P000.jpg')
            time.sleep(kwargs['pano_interval'])
            self.rm.pan.deactivate()
            self.rm.tilt.deactivate()

            return False

        elif kwargs['pano_mode'] == 'Horizontal panorama':
            cont = True

            kwargs['nb_sit_step'] = 1
            kwargs['avct'] = int(kwargs['gis_counter']/kwargs['nb_gis_step']*100)

            self.rm.pan.activate()
            self.rm.tilt.activate()
            apn_path = self.apn.takePicture('pics/photo_G%3.3i_S%3.3i.jpg' % (kwargs['gis_counter'],kwargs['sit_counter']))
            time.sleep(kwargs['pano_interval'])

            if kwargs['gis_counter'] == kwargs['nb_gis_step']:
                cont = False
                kwargs['sit_counter'] = 0
                kwargs['gis_counter'] = 0
                kwargs['avct'] = 0
                self.rm.pan.deactivate()
                self.rm.tilt.deactivate()
            else:
                self.rm.pan.turn(kwargs['gis_step'], speed=2*np.pi/10.)

            kwargs['gis_counter'] += 1

            return cont

        elif kwargs['pano_mode'] == 'Half sphere panorama':
            cont = True

            general_counter = (kwargs['sit_counter']-1)*kwargs['nb_gis_step'] + kwargs['gis_counter']
            nb_step = kwargs['nb_gis_step']*kwargs['nb_sit_step']
            kwargs['avct'] = int(general_counter/nb_step*100)

            self.rm.pan.activate()
            self.rm.tilt.activate()
            apn_path = self.apn.takePicture('pics/photo_G%3.3i_S%3.3i.jpg' % (kwargs['gis_counter'],kwargs['sit_counter']))
            time.sleep(kwargs['pano_interval'])

            if kwargs['gis_counter'] == kwargs['nb_gis_step']:
                kwargs['sit_counter'] += 1
                kwargs['gis_counter'] = 0
                self.rm.tilt.turn(kwargs['sit_step'], speed=2*np.pi/10.)

                kwargs['gis_step'] = kwargs['gis_step0']/np.cos((kwargs['sit_counter']-1)*kwargs['sit_step'])
                kwargs['nb_gis_step'] = int(np.ceil(2*np.pi/kwargs['gis_step']))
            else:
                self.rm.pan.turn(kwargs['gis_step'], speed=2*np.pi/10.)

            if kwargs['sit_counter'] == kwargs['nb_sit_step']+1:
                cont = False

                # Prend en photo le zenit
                self.rm.tilt.turn(np.pi/2-(kwargs['sit_counter']-1)*kwargs['sit_step'], speed=2*np.pi/10.)
                apn_path = self.apn.takePicture()
                time.sleep(kwargs['pano_interval'])
                self.apn.downloadPicture(apn_path, 'pics/photo_G001_S%3.3i.jpg' % kwargs['sit_counter'])
                # FIN Prend en photo le zenit

                kwargs['sit_counter'] = 0
                kwargs['gis_counter'] = 0
                kwargs['avct'] = 0
                self.rm.pan.deactivate()
                self.rm.tilt.deactivate()

            kwargs['gis_counter'] += 1

            return cont

        else:
            return False
