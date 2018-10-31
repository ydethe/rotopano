from RPFirmware.handlers.BaseHandler import BaseHandler
from RPFirmware.RPEphemeris import RPEphemeris
from RPFirmware.ActionManager import ActionManager


class TrackingGUIHandler(BaseHandler):
   def get(self):
      am = ActionManager()
      ac = am.getAction('tracking')
      dat = ac.getState()

      self.render("tracking.html", bodies=RPEphemeris().listBodies(), trk_interval=dat['trk_interval'], trk_duration=dat['trk_duration'])

