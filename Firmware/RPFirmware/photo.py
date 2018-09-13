import time
import os

import gphoto2 as gp

from EnvoiMail import SendMail


context = gp.gp_context_new()
camera = gp.check_result(gp.gp_camera_new())

print('Please connect and switch on your camera')
while True:
    error = gp.gp_camera_init(camera, context)
    if error >= gp.GP_OK:
        # operation completed successfully so exit loop
        break
    if error != gp.GP_ERROR_MODEL_NOT_FOUND:
        # some other error we can't handle here
        raise gp.GPhoto2Error(error)
    # no camera, try again in 2 seconds
    time.sleep(2)
    
# text = gp.check_result(gp.gp_camera_get_summary(camera, context))
# print('Summary')
# print('=======')
# print(text.text)

file_path = gp.check_result(gp.gp_camera_capture(camera, gp.GP_CAPTURE_IMAGE))
print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
target = os.path.join('/tmp', file_path.name)
print('Copying image to', target)
camera_file = gp.check_result(gp.gp_camera_file_get(camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))
gp.check_result(gp.gp_file_save(camera_file, target))

gp.check_result(gp.gp_camera_exit(camera))

SendMail('Test', 'ydethe@gmail.com','ydethe@gmail.com',target)


