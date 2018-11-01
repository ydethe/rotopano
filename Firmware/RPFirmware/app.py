import os
import sys

from tornado.web import url
from tornado.wsgi import WSGIApplication

from RPFirmware.ActionManager import ActionManager

from RPFirmware.handlers.gui.PanoramaGUIHandler import PanoramaGUIHandler
from RPFirmware.handlers.gui.TrackingGUIHandler import TrackingGUIHandler
from RPFirmware.handlers.gui.ConfigGUIHandler import ConfigGUIHandler
from RPFirmware.handlers.state.StateHandler import StateHandler
from RPFirmware.handlers.IndexHandler import IndexHandler

from RPFirmware.Logger import Logger


def make_app():
    app = WSGIApplication(handlers=[
        url(r"/gui/panorama", PanoramaGUIHandler, name='/gui/panorama'),
        url(r"/", IndexHandler, name='/index'),
        url(r"/gui/tracking", TrackingGUIHandler, name='/gui/tracking'),
        url(r"/gui/config", ConfigGUIHandler, name='/gui/config'),
        url(r"/state", StateHandler, name='/state'),
        ],
        debug=True,
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), "static"),
    )
    
    ActionManager()
    
    log = Logger()
    # log.addStream(open(os.path.join(os.path.dirname(__file__), "debug.log"),'a'))
    # log.addStream(sys.stdout)
    
    return app
