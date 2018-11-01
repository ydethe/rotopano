import sys

from singleton3 import Singleton


class Logger (object, metaclass=Singleton):
    def __init__(self):
        self.setStream(sys.stdout)
        
    def setStream(self, f):
        self._stream = f
        
    def log(self, a):
        self._stream.write(a)
        