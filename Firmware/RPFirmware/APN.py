import time
import os

from singleton3 import Singleton
import gphoto2 as gp


class APN (object, metaclass=Singleton):
    def __init__(self):
        self.context = gp.gp_context_new()
        self.camera = gp.check_result(gp.gp_camera_new())
        
        while True:
            error = gp.gp_camera_init(self.camera, self.context)
            if error >= gp.GP_OK:
                # operation completed successfully so exit loop
                break
            if error != gp.GP_ERROR_MODEL_NOT_FOUND:
                # some other error we can't handle here
                raise gp.GPhoto2Error(error)
            # no self.camera, try again in 2 seconds
            time.sleep(2)
            
        self.camera_description = gp.check_result(gp.gp_camera_get_summary(self.camera, self.context))
    
    def getCameraDescription(self):
        return self.camera_description
        
    def takePicture(self):
        u'''Takes a picture with the connected camera.
        
        @return target
            Path to the jpg stored in the camera
        
        '''
        apn_path = gp.check_result(gp.gp_camera_capture(self.camera, gp.GP_CAPTURE_IMAGE))
        
        return apn_path
        
    def downloadPicture(self, apn_path, loc_path):
        camera_file = gp.check_result(gp.gp_camera_file_get(self.camera, apn_path.folder, apn_path.name, gp.GP_FILE_TYPE_NORMAL))
        gp.check_result(gp.gp_file_save(camera_file, loc_path))
        
    def __del__(self):
        gp.check_result(gp.gp_camera_exit(self.camera))
        