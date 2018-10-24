from tornado.web import RequestHandler
from tornado.escape import json_decode

from astropy.coordinates import EarthLocation
import astropy.units as u
import numpy as np

from ..Config import Config
from ..RPEphemeris import RPEphemeris


class TrackingHandler(RequestHandler):
   def get(self):
      cfg = Config()
      self.render("tracking.html", bodies=RPEphemeris.listBodies(), **cfg.getDictionnary())

   def post(self):
      cfg = Config()
      cfg.setDictionnary(self.request.arguments)
      eph = RPEphemeris()
      bdy = eph.getBody(cfg.getParam('trk_body'))
      alt, az, d = eph.getAltAz(bdy, EarthLocation(lat=48.829456*u.deg, lon=2.302180*u.deg, height=0*u.m))
      print("%s : Alt=%.1fdeg, az=%.1fdeg, d=%.1fkm" % (cfg.getParam('trk_body'), alt*180/np.pi,az*180/np.pi,d/1000))
