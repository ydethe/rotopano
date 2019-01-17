from singleton3 import Singleton
import numpy as np


class GPS (object, metaclass=Singleton):
    def __init__(self):
        pass

    def getTpsLatLonAlt(self, prec=10):
        return 0., 0., 0., 0.
        
        