from multiprocessing import Manager

from singleton3 import Singleton

from RPFirmware.Logger import logger
from RPFirmware.resources.APN import APN
from RPFirmware.resources.GPS import GPS
from RPFirmware.resources.RPEphemeris import RPEphemeris
from RPFirmware.resources.Motor import PanMotor, TiltMotor
from RPFirmware.resources.imu_driver import LSM9DS0
from RPFirmware.resources.Clock import Clock


class ResourcesManager (object, metaclass=Singleton):
   def __init__(self):
      self.imu = LSM9DS0()
      logger.info("IMU loaded")
      self.apn = APN()
      logger.info("Camera loaded")
      self.gps = GPS()
      logger.info("GPS loaded")
      self.eph = RPEphemeris()
      logger.info("Ephemeris loaded")
      self.pan = PanMotor()
      logger.info("Pan motor loaded")
      self.tilt = TiltMotor()
      logger.info("Tilt motor loaded")
      self.clk = Clock(5000)
      logger.info("Clock loaded")
