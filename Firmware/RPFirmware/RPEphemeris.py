from singleton3 import Singleton

import numpy as np
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import get_body, solar_system_ephemeris, SkyCoord, EarthLocation, AltAz


class RPEphemeris (object, metaclass=Singleton):
   def __init__(self):
      solar_system_ephemeris.set('builtin')
      # solar_system_ephemeris.set('de430')
      mars = self.getBody('mars')
      _ = self.getAltAz(mars, EarthLocation(lat=0.*u.deg, lon=0.*u.deg, height=0*u.m))

   def getBody(self, name, t=None):
      if t is None:
         t = Time.now()
      if name in RPEphemeris.listBodies():
         bdy = get_body(name, t)
      else:
         bdy = SkyCoord.from_name(name)
      return bdy

   def getAltAz(self, body, loc, t=None):
      if t is None:
         t = Time.now()
      coord = body.transform_to(AltAz(obstime=t,location=loc))
      if coord.distance.unit == '':
         d = 0.
      else:
         d = coord.distance.meter
      return coord.alt.rad, coord.az.rad, d

   @staticmethod
   def listBodies():
      return solar_system_ephemeris.bodies

