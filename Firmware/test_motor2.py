import numpy as np

from RPFirmware.control.RPSimulation import make_simulation
from RPFirmware.ResourcesManager import ResourcesManager


sim = make_simulation()
clk = ResourcesManager().clk
clk.start()

while True:
    pass
