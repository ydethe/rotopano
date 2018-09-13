import unittest

import numpy as np
# import matplotlib.pyplot as plt
# from astropy.visualization import astropy_mpl_style
# plt.style.use(astropy_mpl_style)
import astropy.units as u
from astropy.coordinates import EarthLocation

from RPFirmware.RPEphemeris import RPEphemeris


class TestEphemeris (unittest.TestCase):
   def test_mars(self):
      dorceau = EarthLocation(lat=48.4238969*u.deg, lon=0.8030100*u.deg, height=200*u.m)
      conta   = EarthLocation(lat=45.8227460*u.deg, lon=6.7265530*u.deg, height=200*u.m)
      ici = dorceau
      
      a = RPEphemeris()
      
      mars = a.getBody('mars')
      
      alt,az,d = a.getAltAz(mars, ici)
      print("Mars alt=%.3fdeg, az=%.3fdeg, d=%.0fkm" % (alt*180/np.pi,az*180/np.pi,d/1000))
      
   def test_m31(self):
      dorceau = EarthLocation(lat=48.4238969*u.deg, lon=0.8030100*u.deg, height=200*u.m)
      conta   = EarthLocation(lat=45.8227460*u.deg, lon=6.7265530*u.deg, height=200*u.m)
      ici = dorceau
      
      a = RPEphemeris()
            
      m31 = a.getBody('m31')
      
      alt,az,d = a.getAltAz(m31, ici)
      print("M31 alt=%.3fdeg, az=%.3fdeg, d=%.0fkm" % (alt*180/np.pi,az*180/np.pi,d/1000))
      
      

if __name__ == '__main__':
   unittest.main()
   
   
   