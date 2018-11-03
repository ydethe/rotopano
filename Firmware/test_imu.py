import time

import numpy as np

from RPFirmware.resources.imu_driver import LSM9DS0


a = LSM9DS0()

while True:
    data = a.read()
    print(data.pitch*180/np.pi)
    time.sleep(0.02)
    