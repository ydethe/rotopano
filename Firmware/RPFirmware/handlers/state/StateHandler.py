import os
import json

from RPFirmware.handlers.BaseHandler import BaseHandler
from RPFirmware.ActionManager import ActionManager
from RPFirmware.Logger import Logger


class StateHandler(BaseHandler):
    def get(self):
        args = self.form_to_dict()
        act = ActionManager()

        aa = args['action']

        if not 'action' in args.keys():
            raise KeyError

        dat = act.handleRequest(args)
        
        Logger().log("StateHandler : action=%s, dat=%s\n" % (aa, str(dat)))
        
        self.write(json.dumps(dat))
