import time
import sys

import numpy as np
from matplotlib import pyplot as plt


def main():
   if len(sys.argv) == 1:
      gene_data()
   else:
      plot_data(sys.argv[1])

def plot_data(fic):
   f = open(fic,'r')
   tps = []
   p = []
   cmd = []
   ax = []
   ay = []
   az = []
   gx = []
   gy = []
   gz = []
   mx = []
   my = []
   mz = []
   line = f.readline()

   while line != '':
       ti,pi,ci,gxi,gyi,gzi,axi,ayi,azi,mxi,myi,mzi = [float(x) for x in line.split(',')]
       tps.append(ti)
       p.append(pi)
       cmd.append(ci)
       ax.append(axi)
       ay.append(ayi)
       az.append(azi)
       gx.append(gxi)
       gy.append(gyi)
       gz.append(gzi)
       mx.append(gxi)
       my.append(gyi)
       mz.append(gzi)
       line = f.readline()

   f.close()

   print(np.mean(gx),np.var(gx))
   print(np.mean(gy),np.var(gy))
   print(np.mean(gz),np.var(gz))

   print(np.mean(ax),np.var(ax))
   print(np.mean(ay),np.var(ay))
   print(np.mean(az),np.var(az))

   print(np.mean(mx),np.var(mx))
   print(np.mean(my),np.var(my))
   print(np.mean(mz),np.var(mz))

   fig = plt.figure()
   axe = fig.add_subplot(111)
   axe.grid(True)

   axe.plot(tps,p, label="Mesure")
   axe.plot(tps,cmd, label="Commande")
   axe.legend()

   plt.show()

def gene_data():
   from RPFirmware.resources.imu_driver import LSM9DS0
   from RPFirmware.resources.Motor import TiltMotor, PanMotor

   a = LSM9DS0()

   m = TiltMotor()
   m.setFracStep(16)
   m.activate()

   f = open('data.txt','w')

   ns = 200
   dt = 0.01
   dx = np.pi/ns/2
   cmd = 0.
   tps = 0.

   t0 = time.time()
   while time.time() - t0 < 10.:
      dat = a.read()
      tps += dt
      f.write("%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n" % (tps,dat.pitch*180/np.pi,cmd*180/np.pi,dat.gyr.x,dat.gyr.y,dat.gyr.z,dat.acc.x,dat.acc.y,dat.acc.z,dat.mag.x,dat.mag.y,dat.mag.z))
      time.sleep(dt)
   exit(0)

   for i in range(ns):
      m.turn(dx)
      cmd += dx
      dat = a.read()
      tps += dt
      f.write("%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n" % (tps,dat.pitch*180/np.pi,cmd*180/np.pi,dat.gyr.x,dat.gyr.y,dat.gyr.z,dat.acc.x,dat.acc.y,dat.acc.z,dat.mag.x,dat.mag.y,dat.mag.z))
      time.sleep(dt)

   for i in range(ns):
      m.turn(-dx)
      cmd -= dx
      dat = a.read()
      tps += dt
      f.write("%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n" % (tps,dat.pitch*180/np.pi,cmd*180/np.pi,dat.gyr.x,dat.gyr.y,dat.gyr.z,dat.acc.x,dat.acc.y,dat.acc.z,dat.mag.x,dat.mag.y,dat.mag.z))
      time.sleep(dt)

   f.close()

   m.deactivate()


if __name__ == '__main__':
   main()
