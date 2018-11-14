from matplotlib import pyplot as plt
import numpy as np

from RPFirmware.control.RPSimulation import RPSimulation
from RPFirmware.control.RPController import RPController
from RPFirmware.control.RPEstimator import RPEstimator
from RPFirmware.control.RPSystem import RPSystem
from RPFirmware.control.RPSensors import RPSensors


# COBYLA
P = 4
I = 1.26
J = 120.39401775961012

dt = 0.01
cons = np.array([np.pi/2,np.pi/2])
ctrl = RPController(dt, P, I)
sys = RPSystem()
sensors = RPSensors()
estimator = RPEstimator(dt)
sim = RPSimulation(cons, dt, ctrl, sys, sensors, estimator)

sys.reset()
sim.simulate(20.)
log = sim.getLogger()

fig = plt.figure()
   
axe = fig.add_subplot(211)
axe.grid(True)
log.plot('t', 'tilt*180/np.pi', axe)
log.plot('t', 'tilt*0 + 90', axe, linestyle='--')
axe.set_ylabel("Tilt (deg)")
   
# axe = fig.add_subplot(212, sharex=axe)
# axe.grid(True)
# log.plot('t', 'bais_vpan_est*180/np.pi', axe)
# log.plot('t', 'biais_vtilt_est*180/np.pi', axe)
# log.plot('t', 'bais_vpan_est*0 + 1', axe, linestyle='--')
# log.plot('t', 'bais_vpan_est*0 - 3', axe, linestyle='--')
# axe.set_xlabel("Temps (s)")
# axe.set_ylabel("Biais (deg/s)")

axe = fig.add_subplot(212, sharex=axe)
axe.grid(True)
log.plot('t', 'cmd_tilt*180/np.pi', axe)
log.plot('t', 'cmd_pan*180/np.pi', axe)
axe.set_xlabel("Temps (s)")
axe.set_ylabel("Commande (deg/s)")

plt.savefig('res.png')
plt.show()
