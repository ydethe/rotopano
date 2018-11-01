import time

import numpy as np

from RPFirmware.Motor import Motor
from RPFirmware.pi_settings import *


m = Motor(**pan_motor)

m.setFracStep(16)

m.activate()
m.turn(2*np.pi/7., speed=2*np.pi/10.)

# f = m.setSpeed(2*np.pi)
# print("Vitesse jouée : %.1frad/s" % f)
# time.sleep(2*np.pi/f)

m.deactivate()

