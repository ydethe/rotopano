import time

import numpy as np
from matplotlib import pyplot as plt


f = open('data.txt','r')
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


