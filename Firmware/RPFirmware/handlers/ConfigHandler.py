from tornado.web import RequestHandler

from ..Config import Config


class ConfigHandler(RequestHandler):
   def get(self):
      cfg = Config()
      self.render("config.html", **cfg.getDictionnary())

    def post(self):
        cfg = Config()
        cfg.setDictionnary(self.request.arguments)
