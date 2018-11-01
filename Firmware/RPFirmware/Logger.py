import sys
import os

from singleton3 import Singleton


class Logger (object, metaclass=Singleton):
    def __init__(self):
        self.resetStreams()
        self.addStream(sys.stdout)
        self.addStream(open(os.path.join(os.path.dirname(__file__), "debug.log"),'a'))
        
    def resetStreams(self):
        self._streams = []
        
    def addStream(self, f):
        self._streams.append(f)
        
    def log(self, a):
        for s in self._streams:
            s.write(a)
        