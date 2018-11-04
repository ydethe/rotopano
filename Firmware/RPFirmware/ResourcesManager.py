from singleton3 import Singleton

from RPFirmware.resources.APN import APN
from RPFirmware.resources.GPS import GPS
from RPFirmware.resources.RPEphemeris import RPEphemeris
from RPFirmware.resources.Motor import PanMotor, TiltMotor
from RPFirmware.resources.imu_driver import LSM9DS0


class ResourcesManager (object, metaclass=Singleton):
   def __init__(self):
      self.apn = APN()
      self.gps = GPS()
      self.imu = LSM9DS0()
      self.eph = RPEphemeris()
      self.pan = PanMotor()
      self.tilt = TiltMotor()
      
      
      