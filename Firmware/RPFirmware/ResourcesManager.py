from multiprocessing import Manager

from singleton3 import Singleton

from RPFirmware.resources.APN import APN
from RPFirmware.resources.GPS import GPS
from RPFirmware.resources.RPEphemeris import RPEphemeris
from RPFirmware.resources.Motor import PanMotor, TiltMotor
from RPFirmware.resources.IMU import IMU


class ResourcesManager (object, metaclass=Singleton):
   def __init__(self):
      n = 100
      m = Manager()
    
      tps_buf       = m.Array('d', [0. for _ in range(n)])
      pitch_buf     = m.Array('d', [0. for _ in range(n)])
      raw_pitch_buf = m.Array('d', [0. for _ in range(n)])
    
      self.imu = IMU(n, tps_buf, pitch_buf, raw_pitch_buf)
      self.apn = APN()
      self.gps = GPS()
      self.eph = RPEphemeris()
      self.pan = PanMotor()
      self.tilt = TiltMotor()
      
      
      