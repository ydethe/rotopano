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

        # fic = open('/home/ydethe/mysite/RPFirmware/debug.log','a')
        # fic.write("StateHandler : dat=%s\n" % str(dat))
        # fic.close()

        self.write(json.dumps(dat))
