import math

import numpy as np

from SystemControl.System import ASystem


def find_nearest(array,value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return array[idx-1]
    else:
        return array[idx]
        
class RPSystem (ASystem):
    def __init__(self):
        ASystem.__init__(self, name_of_states=['pan','tilt'])
        self.reset()
        self.lfreq = np.array([10, 20, 40, 50, 80, 100, 160, 200, 250, 320, 400, 500, 800, 1000, 1600, 2000, 4000, 8000])
        self.den = 8
        self.nstp = 200
        self.reduc = 0.75
        self.stp = 2*np.pi/(self.nstp*self.den)
        self.aov = 2*np.arctan(15.6/(2*200))
        self.lim_cmd = self.lfreq[0]*2*np.pi/(self.den*self.nstp)*self.reduc
        self.prec = self.aov / 10.

    def reset(self):
        self.setState(np.array([0.,0.]), 0.)
        
    def behavior(self, x, u, t):
        pan, tilt = x
        cmd_vpan, cmd_vtilt = u
        
        # Conversion commande --> fréquence
        freq_vpan  = np.int(np.abs(cmd_vpan/(2*np.pi)*self.den*self.nstp/self.reduc))
        freq_vtilt = np.int(np.abs(cmd_vtilt/(2*np.pi)*self.den*self.nstp/self.reduc))
        
        # Recherche de la fréquence la plus proche parmi celles possibles sur RPI3B
        freq_vpan  = find_nearest(self.lfreq,freq_vpan)
        freq_vtilt = find_nearest(self.lfreq,freq_vtilt)
        
        # Conversion fréquence --> commande
        if cmd_vpan < 0.:
            vpan  = -freq_vpan*2*np.pi/(self.den*self.nstp)*self.reduc
        else:
            vpan  = freq_vpan*2*np.pi/(self.den*self.nstp)*self.reduc
            
        if cmd_vtilt < 0.:
            vtilt = -freq_vtilt*2*np.pi/(self.den*self.nstp)*self.reduc
        else:
            vtilt = freq_vtilt*2*np.pi/(self.den*self.nstp)*self.reduc
        
        # Dérivée du vecteur d'état
        dx = np.array([vpan,vtilt])
        return dx
        