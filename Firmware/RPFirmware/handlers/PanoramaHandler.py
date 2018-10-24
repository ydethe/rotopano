from .BaseHandler import BaseHandler


class PanoramaHandler(BaseHandler):
    def get(self):
        self.render("panorama.html", pano_modes=['Photo', 'Horizontal panorama', 'Half sphere panorama'], **self.cfg.getDictionnary())

    def post(self):
        self.cfg.setDictionnary(self.form_to_dict())
        self.render("panorama.html", pano_modes=['Photo', 'Horizontal panorama', 'Half sphere panorama'], **self.cfg.getDictionnary())

