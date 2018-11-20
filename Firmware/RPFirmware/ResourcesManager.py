from multiprocessing import Manager

from singleton3 import Singleton

from RPFirmware.resources.APN import APN
from RPFirmware.resources.GPS import GPS
from RPFirmware.resources.RPEphemeris import RPEphemeris
from RPFirmware.resources.Motor import PanMotor, TiltMotor
from RPFirmware.resources.imu_driver import LSM9DS0
from RPFirmware.resources.Clock import Clock


class ResourcesManager (object, metaclass=Singleton):
   def __init__(self):
      self.imu = LSM9DS0()
      self.apn = APN()
      self.gps = GPS()
      self.eph = RPEphemeris()
      self.pan = PanMotor()
      self.tilt = TiltMotor()
      self.clk = Clock(5000)
