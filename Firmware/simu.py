from matplotlib import pyplot as plt
import numpy as np

from RPFirmware.control.RPSimulation import RPSimulation
from RPFirmware.control.RPController import RPController
from RPFirmware.control.RPEstimator import RPEstimator
from RPFirmware.control.RPSystem import RPSystem
from RPFirmware.control.RPSensors import RPSensors


fmax = 8000
den = 8
nstp = 200
reduc = 0.75
stp = 2*np.pi/(nstp*den)
aov = 2*np.arctan(15.6/(2*200))
lim_cmd = fmax*2*np.pi/(den*nstp)*reduc
prec = aov / 10.

# COBYLA
P = 7.51209586
I = 1.97745718

dt = 0.01
cons = np.ones(2)*np.pi/18
ctrl = RPController(dt, P, I)
sys = RPSystem()
sensors = RPSensors()
estimator = RPEstimator(dt)
sim = RPSimulation(cons, dt, ctrl, sys, sensors, estimator)

sys.reset()
sim.simulate(20.)
log = sim.getLogger()
t = log.getValue('t')

iok = np.where(t<10)[0]
t_cons = np.zeros(len(t))
t_cons[iok] = cons[1]

fig = plt.figure()
   
axe = fig.add_subplot(211)
axe.grid(True)
log.plot('t', 'tilt*180/np.pi', axe)
axe.plot(t, t*0 + (t_cons+prec)*180/np.pi, linestyle='--', color='black', label="Tolérance")
axe.plot(t, t*0 + (t_cons-prec)*180/np.pi, linestyle='--', color='black')
axe.set_ylabel("Tilt (deg)")

axe = fig.add_subplot(212, sharex=axe)
axe.grid(True)
log.plot('t', 'cmd_tilt*180/np.pi', axe)
log.plot('t', 'cmd_pan*180/np.pi', axe)
axe.set_xlabel("Temps (s)")
axe.set_ylabel("Commande (deg/s)")

plt.savefig('res.png')
plt.show()
