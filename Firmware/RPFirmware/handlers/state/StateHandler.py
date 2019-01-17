import os
import json

from RPFirmware.handlers.BaseHandler import BaseHandler
from RPFirmware.ActionManager import ActionManager
from RPFirmware.ResourcesManager import ResourcesManager
from RPFirmware.Logger import logger


class StateHandler(BaseHandler):
    def get(self):
        args = self.form_to_dict()
        act = ActionManager()
        rm  = ResourcesManager()

        aa = args['action']

        if not 'action' in args.keys():
            raise KeyError

        dat = act.handleRequest(args)

        # logger.debug("StateHandler : action=%s, dat=%s\n" % (aa, str(dat)))

        self.write(json.dumps(dat))
        