import time
import sys

from scipy.signal import firwin, firwin2, lfilter
import numpy as np
from matplotlib import pyplot as plt


def main():
   plot_data('data.txt')

def plot_data(fic):
   ntaps = 16
   
   f = open(fic,'r')
   lines = f.readlines()
   f.close()
   
   n = len(lines)
   
   tps = np.empty(n)
   p = np.empty(n)
   cmd = np.empty(n)
   ax = np.empty(n)
   ay = np.empty(n)
   az = np.empty(n)
   gx = np.empty(n)
   gy = np.empty(n)
   gz = np.empty(n)
   mx = np.empty(n)
   my = np.empty(n)
   mz = np.empty(n)

   for i in range(n):
      ti,pi,ci,gxi,gyi,gzi,axi,ayi,azi,mxi,myi,mzi = [float(x) for x in lines[i].strip().split(',')]
      tps[i] = ti
      p[i] = pi
      cmd[i] = ci
      ax[i] = axi
      ay[i] = ayi
      az[i] = azi
      gx[i] = gxi
      gy[i] = gyi
      gz[i] = gzi
      mx[i] = gxi
      my[i] = gyi
      mz[i] = gzi
   
   dt = tps[1]-tps[0]
   fs = 1./dt
   pb = firwin(ntaps, 1., window='hamming', pass_zero=True, scale=True, nyq=fs/2)
   
   # ==============================
   # TILT
   # ==============================
   tilt = np.arctan2(-ax,-az)*180/np.pi
   tilt_f = lfilter(pb,[1],tilt)
   v_tilt = gy*180/np.pi
   v_tilt_f = lfilter(pb,[1],v_tilt)
   print("Tilt ", np.mean(tilt_f[ntaps:]),np.var(tilt_f[ntaps:]))
   print("Vtilt", np.mean(v_tilt_f[ntaps:]),np.var(v_tilt_f[ntaps:]))
   
   # ==============================
   # PAN
   # ==============================
   pan = np.arctan2(mx,my)*180/np.pi
   pan_f = lfilter(pb,[1],pan)
   v_pan = gz*180/np.pi
   v_pan_f = lfilter(pb,[1],v_pan)
   print("Pan  ", np.mean(pan_f[ntaps:]),np.var(pan_f[ntaps:]))
   print("Vpan ", np.mean(v_pan_f[ntaps:]),np.var(v_pan_f[ntaps:]))
   
   # ==============================
   # TRACE
   # ==============================
   fig = plt.figure()
   
   axe = fig.add_subplot(211)
   axe.grid(True)
   axe.plot(tps,tilt_f, label="tilt filt")
   axe.plot(tps,pan_f, label="pan filt")
   axe.set_ylabel("Angle (deg)")
   axe.legend()
   
   axe = fig.add_subplot(212,sharex=axe)
   axe.grid(True)
   axe.plot(tps,v_tilt_f, label="Vtilt filt")
   axe.plot(tps,v_pan_f, label="Vpan filt")
   axe.set_ylabel("Vitesse (deg/s)")
   axe.legend()
   
   axe.set_xlabel("Temps (s)")
   
   plt.show()


if __name__ == '__main__':
   main()
