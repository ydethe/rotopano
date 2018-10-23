from tornado.web import RequestHandler

from ..Config import Config


class ConfigHandler(RequestHandler):
   def get(self):
      cfg = Config()
      self.render("RPFirmware/templates/config.html", **cfg.getDictionnary())
      