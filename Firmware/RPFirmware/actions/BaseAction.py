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

    def _work(self):
        raise NotImplementedError()

    def start(self, *kwargs):
        if self.getState() == BaseAction.STOPPED:
            Process.start(self)
            self.state.value = BaseAction.RUNNING

    def stop(self):
        if self.is_alive():
            self.close()
            self.join()
        self.state.value = BaseAction.STOPPED

    def pause(self):
        self.state.value = BaseAction.PAUSED

    def resume(self):
        self.state.value = BaseAction.RUNNING
        