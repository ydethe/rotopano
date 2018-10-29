import json

from RPFirmware.handlers.BaseHandler import BaseHandler
from RPFirmware.ActionManager import ActionManager


class PanoramaStateHandler(BaseHandler):
    def get(self):
        pano_mode = self.get_argument('pano_mode', None)
        pano_interval = float(self.get_argument('pano_interval', None))
        cmd = self.get_argument('cmd', None)

        act = ActionManager().getAction('panorama')
        
        if cmd == 'run':
            act.start(pano_mode=pano_mode, pano_interval=pano_interval)

        dat = act.getStateJSON()

        self.write(json.dumps(dat))
