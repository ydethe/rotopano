from multiprocessing import Process, Value


class BaseAction (Process):
    STOPPED=0
    RUNNING=1
    PAUSED=2
    def __init__(self, name):
        Process.__init__(self, target=self._work)
        self.state = Value('i',BaseAction.STOPPED)
        self.name = name

    def getName(self):
        return self.name

    def getState(self):
        return self.state.value

    def loop(self, **kwargs):
        raise NotImplementedError()

    def _work(self):
        while self.loop(**self.kwargs):
            if self.getState() == BaseAction.RUNNING:
                pass
            elif self.getState() == BaseAction.PAUSED:
                while self.getState() == BaseAction.PAUSED:
                    pass
            elif self.getState() == BaseAction.STOPPED:
                break
        self.stop()

    def start(self, **kwargs):
        self.kwargs = kwargs
        if self.getState() == BaseAction.STOPPED:
            Process.start(self)
            self.state.value = BaseAction.RUNNING

    def pause(self):
        self.state.value = BaseAction.PAUSED

    def resume(self):
        self.state.value = BaseAction.RUNNING
    
    def stop(self):
        self.state.value = BaseAction.STOPPED
        