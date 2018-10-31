from RPFirmware.handlers.BaseHandler import BaseHandler
from RPFirmware.ActionManager import ActionManager


class PanoramaGUIHandler(BaseHandler):
    def get(self):
        am = ActionManager()
        ac = am.getAction('panorama')
        dat = ac.getState()

        self.render("panorama.html", pano_modes=['Photo', 'Horizontal panorama', 'Half sphere panorama'], pano_interval=dat['pano_interval'])
