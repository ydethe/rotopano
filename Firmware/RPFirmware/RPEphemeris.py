from singleton3 import Singleton

import astropy.units as u
from astropy.units import cds
from astropy.time import Time
from astropy.coordinates import get_body, solar_system_ephemeris, SkyCoord, EarthLocation, AltAz


cds.enable()

class RPEphemeris (object, metaclass=Singleton):
   def __init__(self):
      solar_system_ephemeris.set('builtin')
      # solar_system_ephemeris.set('de430')
      mars = self.getBody('mars')
      _ = self.getAltAz(mars, lat=0., lon=0., height=0.)

   def getBody(self, name, t=None):
      if t is None:
         t = Time.now()
      if name in RPEphemeris.listBodies():
         bdy = get_body(name, t)
      else:
         bdy = SkyCoord.from_name(name)
      return bdy

   def getAltAz(self, body, lat=0., lon=0., height=0., t=None):
      if t is None:
         t = Time.now()
      coord = body.transform_to(AltAz(obstime=t,location=EarthLocation(lat=lat*u.deg, lon=lon*u.deg, height=height*u.m),pressure=1*cds.atm))
      if coord.distance.unit == '':
         d = 0.
      else:
         d = coord.distance.value
      return coord.alt.value, coord.az.value, d

   @staticmethod
   def listBodies():
      return solar_system_ephemeris.bodies

