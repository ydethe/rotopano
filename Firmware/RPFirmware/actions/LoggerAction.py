import time
import os

import numpy as np

from RPFirmware.actions.BaseAction import BaseAction
from RPFirmware.Config import Config
from RPFirmware.ResourcesManager import ResourcesManager
from RPFirmware.Logger import logger


class LoggerAction (BaseAction):
    @staticmethod
    def getName():
        return 'logger'

    def __init__(self):
        BaseAction.__init__(self, name=self.getName())
        self.reset()
        self.start()

    def reset(self):
        pth = os.path.join(os.path.dirname(__file__), "..", "debug.log")
        logger.debug("LoggerAction.loop : pth=%s\n" % pth)
        
        f = open(pth, 'r')
        self.kwargs['content'] = f.read()
        f.close()

    def loop(self, kwargs):
        return True
        