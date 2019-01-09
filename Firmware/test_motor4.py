import time

from scipy.signal import firwin
import numpy as np
import matplotlib.pyplot as plt

from RPFirmware.resources.imu_driver import LSM9DS0
from RPFirmware.resources.Motor import TiltMotor
from RPFirmware.control.RPEstimator import RPAngleEstimator


kal = RPAngleEstimator()

# Kp = 7.6
Kp = 1
ntaps = 16
flow = 2
fs = 50.

buffer = np.zeros(ntaps)
ind = 0

imu = LSM9DS0()
m = TiltMotor()
m.setFracStep(16)
m.activate()

h = firwin(ntaps, cutoff=flow, window='hamming', pass_zero=True, nyq=fs/2.)

# ns = 200
# f = np.linspace(0., 0.5, ns)
# z = np.exp(1j*2*np.pi*f)
# p = np.poly1d(h)
# H = p(z)
#
# fig = plt.figure()
#
# axe = fig.add_subplot(211)
# axe.grid(True)
# axe.plot(f, 10*np.log10(np.abs(H)))
# axe.set_ylabel("Amplitude (dB)")
#
# axe = fig.add_subplot(212, sharex=axe)
# axe.grid(True)
# axe.plot(f, np.angle(H)*180/np.pi)
# axe.set_ylabel("Phase (deg)")
# axe.set_xlabel("f/fs")
#
# plt.savefig('bode.png')

logf = open('simu.log','w')

u = 0.
t0 = time.time()
while time.time()-t0 < 30. or True:
    tnew = time.time()

    # Mesure
    dat = imu.read()
    tilt_mes = -np.arctan2(-dat.acc.x, -dat.acc.z)
    vtilt_mes = dat.gyr.y

    # Estimation
    inputs = {'command':np.array([0.,u]), 'measurement':np.array([0.,0.,tilt_mes,vtilt_mes])}
    kal.update(0.,1./fs, inputs)
    _,tilt_est = kal.getState()

    # Filtrage
    buffer[ind] = tilt_mes
    tilt_filt = 0.
    for ifilt in range(ntaps):
        tilt_filt += h[ifilt]*buffer[(-ifilt+ind) % ntaps]
    ind = (ind+1) % ntaps

    # Commande
    u = np.clip(-Kp*tilt_est, -2*np.pi/10,2*np.pi/10)
    m.setSpeed(u)

    # Log
    logf.write('t,%f\n' % (time.time()-t0))
    logf.write('tilt_mes,%f\n' % tilt_mes)
    logf.write('tilt_filt,%f\n' % tilt_filt)
    logf.write('tilt_est,%f\n' % tilt_filt)
    logf.write('cmd_vtilt,%f\n' % u)

    # Cadencement
    while time.time()-tnew < 1./fs:
        pass

m.deactivate()
