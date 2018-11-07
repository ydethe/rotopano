import json

import numpy as np
from singleton3 import Singleton

from RPFirmware.handlers.BaseHandler import BaseHandler
from RPFirmware.ActionManager import ActionManager
from RPFirmware.Logger import logger
from RPFirmware.ResourcesManager import ResourcesManager


class PlotHandler(BaseHandler):
    def get(self, param=''):
        if param == 'gui':
            self.render('plot.html')
        else:
            am = ActionManager()
            ac = am.getAction('plotting')
            state = ac.getState()
            imu = ResourcesManager().imu
            
            args = self.form_to_dict()
            dat = imu.getDataSince(param, args['tps'])
            self.write(json.dumps(dat))
            