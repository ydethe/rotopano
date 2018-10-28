from singleton3 import Singleton

from .actions.PanoramaAction import PanoramaAction


class ActionManager (object, metaclass=Singleton):
    def __init__(self):
        self.handlers = {}
        self.handlers[PanoramaAction.getName()] = PanoramaAction()

    def getAction(self, name):
        return self.handlers[name]