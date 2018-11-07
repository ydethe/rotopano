import time
import os

from RPFirmware.actions.BaseAction import BaseAction
from RPFirmware.ResourcesManager import ResourcesManager
from RPFirmware.Logger import logger


class PlottingAction (BaseAction):
    @staticmethod
    def getName():
        return 'plotting'

    def __init__(self):
        self.rm = ResourcesManager()
        self.imu = self.rm.imu
        BaseAction.__init__(self, name=self.getName())
        self.reset()
        
    def reset(self):
        self.kwargs['t_start'] = time.time()
        
    def loop(self, kwargs):
        cont = True

        self.imu.measure(kwargs['t_start'])
        
        time.sleep(0.02)

        return cont
        
        