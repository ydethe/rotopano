import time
import os

from singleton3 import Singleton
import gphoto2 as gp

from RPFirmware.resources.EXIF import set_gps_location
from RPFirmware.resources.GPS import GPS
from RPFirmware.Logger import logger


class APN (object, metaclass=Singleton):
    def __init__(self):
        self.context = gp.gp_context_new()
        self.camera = gp.check_result(gp.gp_camera_new())

    def connect(self):
        gp.gp_camera_exit(self.camera, self.context)

        logger.debug("Trying to connect to the camera...")
        for ic in range(1000):
            logger.debug("   Attempt %i/10" % (ic+1))
            time.sleep(0.2)
            error = gp.gp_camera_init(self.camera, self.context)
            if error == gp.GP_OK:
                # operation completed successfully so exit loop
                self.camera_description = str(gp.check_result(gp.gp_camera_get_summary(self.camera, self.context)))
                logger.debug("Camera connected")
                return True

            # no self.camera, try again in 2 seconds
            gp.gp_camera_exit(self.camera, self.context)

        # raise gp.GPhoto2Error(error)
        logger.debug("Failed to connect camera")
        time.sleep(0.5)
        return False

    def getCameraDescription(self):
        return self.camera_description

    def takePicture(self, loc_path):
        u'''Takes a picture with the connected camera.

        @return target
            Path to the jpg stored in the camera

        '''
        logger.debug("Taking picture...")
        if self.connect():
            apn_path = gp.check_result(gp.gp_camera_capture(self.camera, gp.GP_CAPTURE_IMAGE))
            # g = GPS()
            # tps,lat,lon,alt = g.getTpsLatLonAlt()
            # apn_path.gps_coords = (tps,lat,lon,alt)

            logger.debug("Downloading picture %s/%s ..." % (apn_path.folder, apn_path.name))
            camera_file = gp.check_result(gp.gp_camera_file_get(self.camera, apn_path.folder, apn_path.name, gp.GP_FILE_TYPE_NORMAL))
            gp.check_result(gp.gp_file_save(camera_file, loc_path))
            # tps,lat,lon,alt = apn_path.gps_coords
            # set_gps_location(loc_path, lat, lon, alt)
            logger.info("Picture downloaded")

    def __del__(self):
        gp.check_result(gp.gp_camera_exit(self.camera))


if __name__ == '__main__':
      a = APN()
      a.takePicture()
