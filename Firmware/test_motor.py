import time

import numpy as np
from RPFirmware.resources.imu_driver import LSM9DS0

from RPFirmware.resources.Motor import TiltMotor, PanMotor


# m = PanMotor()
m = TiltMotor()

m.setFracStep(16)

m.activate()

imu = LSM9DS0()

# m.turn(20*np.pi/180, speed=2*np.pi/10.)

t0 = time.time()

while True:
    dat = imu.read()
    print(dat.pitch*180/np.pi)

    dt = time.time()-t0
    if dt > 2:
        break
        
m.turn(-dat.pitch, speed=2*np.pi/10.)

# f = m.setSpeed(2*np.pi)
# print("Vitesse jouée : %.1frad/s" % f)
# time.sleep(2*np.pi/f)

m.deactivate()

