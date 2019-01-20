

class BaseAction (object):
    def __init__(self, name):
        self.kwargs = dict()
        self.name = name

    def getName(self):
        return self.name

    def getActivity(self):
        return 'RUNNING'

    def getState(self):
        return dict(**self.kwargs)

    def reset(self):
        raise NotImplementedError()

    def loop(self, kwargs):
        raise NotImplementedError()

    def start(self, kwargs_opt={}):
        self.reset()
        self.kwargs.update(**kwargs_opt)
        kwargs = dict(**self.kwargs)
        while self.loop(kwargs):
            pass

    def pause(self):
        raise NotImplementedError()

    def resume(self):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()
