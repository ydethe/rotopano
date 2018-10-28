from RPFirmware.handlers.BaseHandler import BaseHandler
from RPFirmware.ActionManager import ActionManager

import sys;print(sys.path)

class PanoramaGUIHandler(BaseHandler):
    def get(self):
        act = ActionManager().getAction('panorama')
        self.render("panorama.html", test=act.counter.value, pano_modes=['Photo', 'Horizontal panorama', 'Half sphere panorama'], **self.cfg.getDictionnary())

    def post(self):
        act = ActionManager().getAction('panorama')
        self.cfg.setDictionnary(self.form_to_dict())
        self.render("panorama.html", test=act.counter.value, pano_modes=['Photo', 'Horizontal panorama', 'Half sphere panorama'], **self.cfg.getDictionnary())

        act.start()
