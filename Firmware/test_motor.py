import time

import numpy as np
from RPFirmware.resources.imu_driver import LSM9DS0

from RPFirmware.resources.Motor import TiltMotor, PanMotor


# m = PanMotor()
m = TiltMotor()

m.setFracStep(16)

m.activate()

imu = LSM9DS0()
dt = 0.05
time.sleep(32*dt)

# m.turn(20*np.pi/180, speed=2*np.pi/10.)

t0 = time.time()

m.turn(0.5)
while True:
    dat = imu.read()
    print(dat.pitch*180/np.pi)
    time.sleep(dt)
    
    dt = time.time()-t0
    if dt > 10:
        break
        
    # m.turn(-dat.pitch, speed=2*np.pi/10.)
    m.setSpeed(-dat.pitch*2)
    
# f = m.setSpeed(2*np.pi)
# print("Vitesse jouée : %.1frad/s" % f)
# time.sleep(2*np.pi/f)

m.deactivate()

