import os
import sys
from multiprocessing import Manager

from tornado.web import url
from tornado.wsgi import WSGIApplication

from RPFirmware.ActionManager import ActionManager

from RPFirmware.handlers.gui.PanoramaGUIHandler import PanoramaGUIHandler
from RPFirmware.handlers.gui.TrackingGUIHandler import TrackingGUIHandler
from RPFirmware.handlers.gui.LoggerGUIHandler import LoggerGUIHandler
from RPFirmware.handlers.gui.ConfigGUIHandler import ConfigGUIHandler
from RPFirmware.handlers.state.StateHandler import StateHandler
from RPFirmware.handlers.IndexHandler import IndexHandler
# from RPFirmware.handlers.gui.PlotHandler import PlotHandler

from RPFirmware.ResourcesManager import ResourcesManager


def make_app():
    ActionManager()
    ResourcesManager()

    am = ActionManager()
    
    app = WSGIApplication(handlers=[
        url(r"/gui/panorama", PanoramaGUIHandler, name='/gui/panorama'),
        url(r"/", IndexHandler, name='/index'),
        # url(r"/gui/tracking", TrackingGUIHandler, name='/gui/tracking'),
        url(r"/gui/logger", LoggerGUIHandler, name='/gui/logger'),
        url(r"/gui/config", ConfigGUIHandler, name='/gui/config'),
        url(r"/state", StateHandler, name='/state'),
        # url(r"/plot/(.*)?/?", PlotHandler, name='plot'),
        ],
        debug=True,
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), "static"),
    )

    return app
