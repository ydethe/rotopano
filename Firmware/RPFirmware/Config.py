import os
import json

from singleton3 import Singleton


def will_it_float(s):
   try:
      float(s)
      return True
   except ValueError:
      return False

class Config (object, metaclass=Singleton):
   PATH=os.path.join(os.path.dirname(__file__), "config.cfg")
   def __init__(self):
      self._data = {'sensor_vsize_mm':15.6, 'sensor_hsize_mm':23.7, 'focal_length_mm':18.,'overlap_p100':20.}
      if os.path.exists(Config.PATH):
         f = open(Config.PATH, 'r')
         self._data.update(json.load(f))
         f.close()
      else:
         self.saveConf()

   def getDictionnary(self):
      return self._data.copy()

   def getIterable(self):
       return self._data.copy()

   def setDictionnary(self, dat):
      for key in dat.keys():
         value = dat.get(key)
         if will_it_float(value):
            self.setParam(key, float(value))
         elif value != '' and not value is None:
            self.setParam(key, value)

   def saveConf(self):
      f = open(Config.PATH, 'w')
      json.dump(self._data, f)
      f.close()

   def getParamList(self):
      return self._data.keys()

   def setParam(self, key, val):
      self._data[key] = val
      self.saveConf()

   def getParam(self, key):
      return self._data[key]

   def __repr__(self):
      s = ""
      for k in self.getParamList():
         s = s + "%s\t: %s\n" % (k, str(self.getParam(k)))
      s = s + ""

      return s

