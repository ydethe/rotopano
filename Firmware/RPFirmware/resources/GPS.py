import gpsd
from singleton3 import Singleton
import numpy as np


class GPS (object, metaclass=Singleton):
   def __init__(self):
      gpsd.connect(host="127.0.0.1", port=2947)
      
   def getTpsLatLonAlt(self, prec=10):
      # Get gps position
      packet = gpsd.get_current()
      err = prec+1
      while packet.mode != 3 or err > prec:
         if 'x' in packet.error:
            elat = packet.error['y']
            elon = packet.error['x']
            err = np.sqrt(elat**2 + elon**2)
         else:
            err = prec+1
         packet = gpsd.get_current()
         
      # See the inline docs for GpsResponse for the available data
      return packet.time, packet.lat, packet.lon, packet.alt
