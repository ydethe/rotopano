from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import minimize

from RPFirmware.control.RPSimulation import RPSimulation
from RPFirmware.control.RPController import RPController
from RPFirmware.control.RPEstimator import RPEstimator
from RPFirmware.control.RPSystem import RPSystem
from RPFirmware.control.RPSensors import RPSensors


dt = 0.01
cons = np.array([np.pi/2,np.pi/2])
sys = RPSystem()
sensors = RPSensors()
estimator = RPEstimator(dt)

def simu(P,I):
    np.random.seed(1253767)
    ctrl = RPController(dt, P, I)
    sys.reset()
    estimator.reset()
    
    sim = RPSimulation(cons, dt, ctrl, sys, sensors, estimator)
    sim.simulate(10.)
    log = sim.getLogger()
    
    return log
    
def cout(X):
    P,I = X
    log = simu(P,I)
    
    t = log.getValue('t')
    tend = t[-1]
    tilt = log.getValue('tilt')
    log.reset()
    
    J = np.sum((tilt-np.pi/2)**2*(t-tend/2)**2)
    print("P,I,J", P,I,J)
    
    return J
    
def cmde_tilt_1(X):
    P,I = X
    log = simu(P,I)
    
    u = log.getValue('cmd_tilt')
    
    return lim_cmd-np.max(u)

def cmde_tilt_2(X):
    P,I = X
    log = simu(P,I)
    
    u = log.getValue('cmd_tilt')
    
    return np.min(u)+lim_cmd

fmax = 8000
den = 8
nstp = 200
reduc = 0.75
stp = 2*np.pi/(nstp*den)
aov = 2*np.arctan(15.6/(2*200))
lim_cmd = fmax*2*np.pi/(den*nstp)*reduc
prec = aov / 10.
print("Commande max : %.3fdeg/s" % (lim_cmd*180/np.pi))
print("Pas : %.3fdeg" % (stp*180/np.pi))
print("AoV : %.2fdeg" % (aov*180/np.pi))
print("Précision visée : %.2fdeg" % (prec*180/np.pi))

meth = 'COBYLA'
res = minimize(cout, np.array([7.51209586, 1.97745718]), constraints=[{'type':'ineq','fun':cmde_tilt_1},{'type':'ineq','fun':cmde_tilt_2}], method=meth)
print(res)

P,I = res.x
log = simu(P,I)
t = log.getValue('t')

fig = plt.figure()
   
axe = fig.add_subplot(211)
axe.grid(True)
log.plot('t', 'tilt*180/np.pi', axe)
log.plot('t', 'tilt*0 + 90', axe, linestyle='--')
axe.plot(t, (cons[1]+prec)*180/np.pi, linestyle='--')
axe.plot(t, (cons[1]-prec)*180/np.pi, linestyle='--')
axe.set_ylabel("Tilt (deg)")
   
axe = fig.add_subplot(212, sharex=axe)
axe.grid(True)
log.plot('t', 'bais_vpan_est*180/np.pi', axe)
log.plot('t', 'biais_vtilt_est*180/np.pi', axe)
log.plot('t', 'bais_vpan_est*0 + 1', axe, linestyle='--')
log.plot('t', 'bais_vpan_est*0 - 3', axe, linestyle='--')
axe.set_xlabel("Temps (s)")
axe.set_ylabel("Biais (deg/s)")

plt.show()


