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
   line = f.readline()
   
   while line != '':
       ti,pi = [float(x) for x in line.split(',')]
       tps.append(ti)
       p.append(pi)
       line = f.readline()
       
   f.close()
   
   fig = plt.figure()
   axe = fig.add_subplot(111)
   axe.grid(True)
   
   axe.plot(tps,p)
   
   plt.show()
   
def gene_data():
   from RPFirmware.resources.IMU import IMU
   a = IMU()
   
   f = open('data.txt','w')
   
   dt = 0.2
   ns = 1000
   for i in range(ns):
      dat = a.read()
      f.write("%f,%f\n" % (i*dtdat.pitch*180/np.pi))
      time.sleep(dt)

   f.close()
   
if __name__ == '__main__':
   main()
