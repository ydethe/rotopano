from RPFirmware.handlers.BaseHandler import BaseHandler
from RPFirmware.RPEphemeris import RPEphemeris


class TrackingGUIHandler(BaseHandler):
   def get(self):
      self.render("tracking.html", bodies=RPEphemeris.listBodies(), **self.cfg.getDictionnary())

