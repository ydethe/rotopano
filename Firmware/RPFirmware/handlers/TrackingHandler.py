from astropy.coordinates import EarthLocation
import astropy.units as u
import numpy as np

from .BaseHandler import BaseHandler
from ..RPEphemeris import RPEphemeris


class TrackingHandler(BaseHandler):
   def get(self):
      self.render("tracking.html", coor="", bodies=RPEphemeris.listBodies(), **self.cfg.getDictionnary())

   def post(self):
      self.cfg.setDictionnary(self.form_to_dict())
      eph = RPEphemeris()
      bdy = eph.getBody(self.cfg.getParam('trk_body'))
      alt, az, d = eph.getAltAz(bdy, EarthLocation(lat=48.829456*u.deg, lon=2.302180*u.deg, height=0*u.m))
      coor = "%s : Alt=%.1fdeg, az=%.1fdeg, d=%.1fkm" % (self.cfg.getParam('trk_body'), alt*180/np.pi,az*180/np.pi,d/1000)
      self.render("tracking.html", coor=coor, bodies=RPEphemeris.listBodies(), **self.cfg.getDictionnary())
