class Observable (object):
    def __init__(self):
        self.observers = []
        
    def addObserver(self, obs):
        self.observers.append(obs)
        
    def notify(self, msg):
        for o in self.observers:
            o.handleMsg(msg)
            
            
class Observer (object):
    def __init__(self):
        pass
        
    def handleMsg(self, msg):
        print(msg)
        
        