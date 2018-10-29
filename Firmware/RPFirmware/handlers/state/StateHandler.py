import json

from RPFirmware.handlers.BaseHandler import BaseHandler
from RPFirmware.ActionManager import ActionManager


class StateHandler(BaseHandler):
    def get(self):
        args = self.form_to_dict()
        act = ActionManager()
        
        if not 'action' in args.keys():
            raise KeyError
        
        dat = act.handleRequest(args)
        
        self.write(json.dumps(dat))
        