import signal

from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.httpserver import HTTPServer

from .app import make_app


def sig_exit(signum, frame):
   IOLoop.instance().add_callback_from_signal(do_stop)
   
def do_stop(*args, **kwargs):
   IOLoop.instance().stop()
   
define('port', default=8888, help='port to listen on')

def main():
   app = make_app()
   http_server = HTTPServer(app)
   http_server.listen(options.port)
   
   signal.signal(signal.SIGTERM, sig_exit)
   signal.signal(signal.SIGINT, sig_exit)
   
   IOLoop.instance().start()
   
if __name__ == '__main__':
   main()
   
   