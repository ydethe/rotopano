import time
from multiprocessing import Process, Value, Manager


class BaseAction (object):
    STOPPED=0
    RUNNING=1
    PAUSED=2
    def __init__(self, name):
        manager = Manager()
        self.activity = Value('i',BaseAction.STOPPED)
        self.kwargs = manager.dict()
        self.name = name
        self._proc = Process(target=self._work, args=(self.activity, self.kwargs))
        self._proc.start()

    def getName(self):
        return self.name

    def getActivity(self):
        return self.activity.value

    def getState(self):
        res = {}

        st = self.getActivity()
        if st == BaseAction.STOPPED:
            res['activity'] = 'STOPPED'
        elif st == BaseAction.RUNNING:
            res['activity'] = 'RUNNING'
        elif st == BaseAction.PAUSED:
            res['activity'] = 'PAUSED'

        res.update(self.kwargs)

        return res

    def reset(self, kwargs):
        raise NotImplementedError()

    def loop(self, kwargs):
        raise NotImplementedError()

    def _work(self, activity,kwargs):
        while True:
            time.sleep(1)
            if activity.value == BaseAction.RUNNING:
                if not self.loop(kwargs):
                    self.stop()
            elif activity.value == BaseAction.PAUSED:
                while activity.value == BaseAction.PAUSED:
                    pass
            elif activity.value == BaseAction.STOPPED:
                pass
            else:
                raise KeyError(activity.value)

    def start(self, kwargs):
        self.kwargs.update(kwargs)
        self.reset(kwargs)
        self.activity.value = BaseAction.RUNNING

    def pause(self):
        self.activity.value = BaseAction.PAUSED

    def resume(self):
        self.activity.value = BaseAction.RUNNING

    def stop(self):
        self.activity.value = BaseAction.STOPPED
