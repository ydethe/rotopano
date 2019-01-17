import os

from singleton3 import Singleton


class RPEphemeris (object, metaclass=Singleton):
    def __init__(self):
        pass

    def getBody(self, name, t=None):
        pass

    def getAltAz(self, name, lat=0., lon=0., height=0., t=None):
        return 0., 0., 0.

    def listBodies(self):
        return ['Moon']
        
        