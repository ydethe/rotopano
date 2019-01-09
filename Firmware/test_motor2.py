import time
import sys;sys.path = ['.'] + sys.path

import numpy as np

from RPFirmware.control.RPSimulation import make_simulation
from RPFirmware.ResourcesManager import ResourcesManager


rm = ResourcesManager()
sim = make_simulation()
clk = rm.clk
rm.tilt.setFracStep(16)
rm.tilt.activate()

# rm.pan.setFracStep(16)
# rm.pan.activate()
# rm.pan.turn(2*np.pi)
# rm.pan.deactivate()
# exit(0)

t0 = time.time()
t = 0.
n = 100
while time.time()-t0 < 30.:
# for k in range(n):
    tnew = time.time()-t0
    sim.update(t, tnew)
    while time.time()-t0-tnew < 0.02:
        pass
    t = tnew
# print((time.time()-t0)/n)

# clk.start()
# t0 = time.time()
# while time.time() - t0 < 10.:
#     pass

rm.tilt.deactivate()
