import time

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

clk.start()

t0 = time.time()
while time.time() - t0 < 10.:
    pass

rm.tilt.deactivate()
