from tornado.web import RequestHandler

from ..Config import Config


class PanoramaHandler(RequestHandler):
   def get(self):
      cfg = Config()
      self.render("panorama.html", pano_modes=['Photo', 'Horizontal panorama', 'Half sphere panorama'], **cfg.getDictionnary())
      