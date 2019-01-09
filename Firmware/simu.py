from matplotlib import pyplot as plt
import numpy as np

from RPFirmware.control.RPSimulation import RPSimulation



sim = RPSimulation()
log = sim.getLogger()
log.setOutputLoggerFile('simu.log')

sim.simulate(np.arange(0.,20.,0.02))
t = log.getValue('t')

fig = plt.figure()

axe = fig.add_subplot(212)
axe.grid(True)
log.plot('t', 'tilt*180/np.pi', axe)
log.plot('t', 'tilt_est*180/np.pi', axe)
log.plot(t, '(tilt_cons+%f)*180/np.pi' % sim.prec, axe, linestyle='--', color='black', label="Tolérance")
log.plot(t, '(tilt_cons-%f)*180/np.pi' % sim.prec, axe, linestyle='--', color='black')
axe.set_ylabel("Tilt (deg)")

plt.savefig('res.png')
plt.show()
