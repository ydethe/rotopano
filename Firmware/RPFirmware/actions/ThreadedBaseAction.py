from multiprocessing import Process, Manager


class ThreadedBaseAction (object):
    def __init__(self, name):
        manager = Manager()
        self.kwargs = manager.dict()
        self.kwargs['activity'] = 'STOPPED'
        self.name = name
        self._proc = Process(target=self._work, args=(self.kwargs,))
        self._proc.start()

    def getName(self):
        return self.name

    def getActivity(self):
        return self.kwargs['activity']

    def getState(self):
        return dict(**self.kwargs)

    def reset(self):
        raise NotImplementedError()

    def loop(self, kwargs):
        raise NotImplementedError()

    def _work(self, kwargs):
        while True:
            a = kwargs['activity']
            if a == 'RUNNING':
                if not self.loop(kwargs):
                    self.stop()
            elif a == 'PAUSED':
                while kwargs['activity'] == 'PAUSED':
                    pass
            elif a == 'STOPPED':
                pass
            else:
                raise KeyError(a)

    def start(self, kwargs={}):
        self.kwargs.update(**kwargs)
        self.reset()
        self.kwargs['activity'] = 'RUNNING'

    def pause(self):
        self.kwargs['activity'] = 'PAUSED'

    def resume(self):
        self.kwargs['activity'] = 'RUNNING'

    def stop(self):
        self.kwargs['activity'] = 'STOPPED'
