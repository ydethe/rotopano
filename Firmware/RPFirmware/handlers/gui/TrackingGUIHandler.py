from RPFirmware.handlers.BaseHandler import BaseHandler
from RPFirmware.ActionManager import ActionManager
from RPFirmware.ResourcesManager import ResourcesManager


class TrackingGUIHandler(BaseHandler):
   def get(self):
      rm = ResourcesManager()
      am = ActionManager()
      ac = am.getAction('tracking')
      dat = ac.getState()

      self.render("tracking.html", bodies=rm.eph.listBodies(), trk_interval=dat['trk_interval'], trk_duration=dat['trk_duration'])

