import numpy as np

from SystemControl.System import ASystem


class RPSystem (ASystem):
    def __init__(self):
        ASystem.__init__(self, name_of_states=['pan','tilt'])
        self.reset()
        
    def reset(self):
        self.setState(np.array([0.,0.]), 0.)
        
    def behavior(self, x, u, t):
        pan, tilt = x
        cmd_vpan, cmd_vtilt = u
        dx = np.array([cmd_vpan,cmd_vtilt])
        return dx
        