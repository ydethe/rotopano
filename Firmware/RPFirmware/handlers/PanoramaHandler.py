from .BaseHandler import BaseHandler
from ..ActionManager import ActionManager


class PanoramaHandler(BaseHandler):
    def get(self):
        act = ActionManager().getAction('panorama')
        self.render("panorama.html", test=act.counter.value, pano_modes=['Photo', 'Horizontal panorama', 'Half sphere panorama'], **self.cfg.getDictionnary())

    def post(self):
        act = ActionManager().getAction('panorama')
        self.cfg.setDictionnary(self.form_to_dict())
        self.render("panorama.html", test=act.counter.value, pano_modes=['Photo', 'Horizontal panorama', 'Half sphere panorama'], **self.cfg.getDictionnary())

        act.start()
