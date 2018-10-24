from tornado.web import RequestHandler

from ..Config import Config, will_it_float


class BaseHandler(RequestHandler):
    def __init__(self, *args, **kwargs):
        RequestHandler.__init__(self, *args, **kwargs)
        self.cfg = Config()

    def form_to_dict(self):
        res  = {}
        for k in self.request.arguments.keys():
            v = self.request.arguments[k]
            if hasattr(v, '__iter__'):
                v = v[0]
            if not will_it_float(v):
                v = v.decode('utf-8')
            res[k] = v
        return res
