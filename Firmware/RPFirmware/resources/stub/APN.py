import time
import os

from singleton3 import Singleton

from RPFirmware.resources.stub.EXIF import set_gps_location
from RPFirmware.resources.stub.GPS import GPS
from RPFirmware.Logger import logger


class APN (object, metaclass=Singleton):
    def __init__(self):
        pass
        
    def connect(self):
        self.camera_description = 'camera_stub'
        self.conn = True
        return True

    def getCameraDescription(self):
        return self.camera_description

    def takePicture(self):
        u'''Takes a picture with the connected camera.

        @return target
            Path to the jpg stored in the camera

        '''
        return './stub.jpg'

    def downloadPicture(self, apn_path, loc_path):
        print("DL photo %s" % loc_path)
        return
        

if __name__ == '__main__':
      a = APN()
      a.takePicture()
