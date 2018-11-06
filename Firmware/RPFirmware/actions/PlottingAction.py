import time
import os

from RPFirmware.actions.BaseAction import BaseAction
from RPFirmware.resources.IMU import IMU
from RPFirmware.Logger import logger


class PlottingAction (BaseAction):
    @staticmethod
    def getName():
        return 'plotting'

    def __init__(self):
        BaseAction.__init__(self, name=self.getName())
        
    def reset(self):
        self.kwargs['t_start'] = time.time()
        self.imu = IMU()
        
    def loop(self, kwargs):
        cont = True

        self.imu.measure(kwargs['t_start'])
        
        time.sleep(0.02)

        return cont
        
        