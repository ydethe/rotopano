from RPFirmware.handlers.BaseHandler import BaseHandler
from RPFirmware.ActionManager import ActionManager


class PanoramaGUIHandler(BaseHandler):
    def get(self):
        act = ActionManager().getAction('panorama')
        state = act.getState()
        self.render("panorama.html", pano_modes=['Photo', 'Horizontal panorama', 'Half sphere panorama'], **self.cfg.getDictionnary(), **state)
