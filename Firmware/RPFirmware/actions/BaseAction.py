from multiprocessing import Process, Value, Manager


class BaseAction (Process):
    STOPPED=0
    RUNNING=1
    PAUSED=2
    def __init__(self, name):
        manager = Manager()
        self.activity = Value('i',BaseAction.STOPPED)
        self.kwargs = manager.dict()
        self.name = name
        Process.__init__(self)
        Process.start(self)
        
    def getName(self):
        return self.name
        
    def getActivity(self):
        return self.activity.value
        
    def getState(self):
        res  = {}

        st = self.getActivity()
        if st == BaseAction.STOPPED:
            res['activity'] = 'STOPPED'
        elif st == BaseAction.RUNNING:
            res['activity'] = 'RUNNING'
        elif st == BaseAction.PAUSED:
            res['activity'] = 'PAUSED'
        
        return res
        
    def reset(self):
        raise NotImplementedError()
        
    def loop(self):
        raise NotImplementedError()

    def run(self):
        while True:
            if self.getActivity() == BaseAction.RUNNING:
                print("RUNNING")
                if not self.loop():
                    self.stop()
            elif self.getActivity() == BaseAction.PAUSED:
                print("PAUSED")
                while self.getActivity() == BaseAction.PAUSED:
                    pass
            elif self.getActivity() == BaseAction.STOPPED:
                print("STOPPED")
                pass
            else:
                raise KeyError(self.getActivity())

    def start(self, **kwargs):
        self.kwargs = kwargs
        self.reset()
        self.activity.value = BaseAction.RUNNING

    def pause(self):
        self.activity.value = BaseAction.PAUSED

    def resume(self):
        self.activity.value = BaseAction.RUNNING
    
    def stop(self):
        self.activity.value = BaseAction.STOPPED
        