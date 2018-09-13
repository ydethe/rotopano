import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math


class IMUTest (object):
   def __init__(self):
      SETTINGS_FILE = "RTIMULib"
      
      print("Using settings file " + SETTINGS_FILE + ".ini")
      if not os.path.exists(SETTINGS_FILE + ".ini"):
        print("Settings file does not exist, will be created")
      
      s = RTIMU.Settings(SETTINGS_FILE)
      self.imu = RTIMU.RTIMU(s)
      
      print("IMU Name: " + self.imu.IMUName())
      
      if (not self.imu.IMUInit()):
         print("IMU Init Failed")
         sys.exit(1)
      else:
         print("IMU Init Succeeded")
      
      # this is a good time to set any fusion parameters
      self.imu.setSlerpPower(0.02)
      self.imu.setGyroEnable(True)
      self.imu.setAccelEnable(True)
      self.imu.setCompassEnable(True)
      
      self.poll_interval = self.imu.IMUGetPollInterval()
      print("Recommended Poll Interval: %dmS\n" % self.poll_interval)
      
      time.sleep(0.05)
      
      self.read()
      while False:
         self.read()
         
   def read(self):
       if self.imu.IMURead():
          data = self.imu.getIMUData()
          fusionPose = data["fusionPose"]
          print("r: %f p: %f y: %f" % (math.degrees(fusionPose[0]), math.degrees(fusionPose[1]), math.degrees(fusionPose[2])))
          time.sleep(self.poll_interval*1.0/1000.0)

      
a = IMUTest()
while True:
   a.read()