from collections import deque
import time

from singleton3 import Singleton
from scipy.signal import firwin
import numpy as np


class IMU (object, metaclass=Singleton):
    def __init__(self, len_buf, tps_buf, pitch_buf, raw_pitch_buf):
        self.pitch = pitch_buf
        self.raw_pitch = raw_pitch_buf
        self.tps = tps_buf
        self.idx = 0
        self.nbuf = len_buf
        
        self.ntaps = 32
        self.fir = firwin(self.ntaps, 0.05, window='hamming')
        
    def measure(self, t_start):
        t = time.time()-t_start
        
        # p = np.random.normal()
        p = np.random.normal()/4+np.cos(t)
        # p = np.cos(t)
        
        self.tps[self.idx] = t
        
        self.raw_pitch[self.idx] = p
    
        fp = 0.
        for i in range(self.ntaps):
            k = (i-self.ntaps//2+self.idx) % self.nbuf
            fp += self.raw_pitch[k]*self.fir[i]
        
        self.pitch[self.idx] = fp
        
        self.idx += 1
        if self.idx == self.nbuf:
            self.idx = 0
        
    def getDataSince(self, type, tps):
        t = np.array(self.tps)
        iok = np.where(t> tps)[0]
        
        x = []
        y = []
        yf = []
        
        for i in iok:
            if type == 'pitch':
                d  = self.pitch[i]
                fd = self.raw_pitch[i]
            elif type == 'roll':
                d  = self.roll[i]
                fd = self.raw_roll[i]
            elif type == 'yaw':
                d  = self.yaw[i]
                fd = self.raw_yaw[i]
                
            x.append(t[i])
            y.append(d)
            yf.append(fd)
            
        return {'x':x, 'y':y, 'yf':yf, 'length':len(iok)}
        
        