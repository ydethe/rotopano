import os
import sys
from multiprocessing import Manager

from tornado.wsgi import WSGIApplication

from RPFirmware.ActionManager import ActionManager
from RPFirmware.handlers.gui.PlotHandler import PlotHandler
from RPFirmware.resources.IMU import IMU


def make_app():
    n = 100
    m = Manager()
    
    tps_buf       = m.Array('d', [0. for _ in range(n)])
    pitch_buf     = m.Array('d', [0. for _ in range(n)])
    raw_pitch_buf = m.Array('d', [0. for _ in range(n)])
    
    imu = IMU(n, tps_buf, pitch_buf, raw_pitch_buf)
    
    am = ActionManager()
    ac = am.getAction('plotting')
    ac.start({})
    
    app = WSGIApplication(handlers=[
        (r"/plot/(.*)?/?", PlotHandler),
        ],
        debug=True,
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), "static"),
    )
    
    return app
