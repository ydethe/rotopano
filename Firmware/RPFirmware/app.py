import os

from tornado.web import url
from tornado.wsgi import WSGIApplication

from RPFirmware.handlers.gui.PanoramaGUIHandler import PanoramaGUIHandler
from RPFirmware.handlers.gui.TrackingGUIHandler import TrackingGUIHandler
from RPFirmware.handlers.gui.ConfigGUIHandler import ConfigGUIHandler
from RPFirmware.handlers.IndexHandler import IndexHandler


def make_app():
   app = WSGIApplication(handlers=[
         url(r"/gui/panorama", PanoramaGUIHandler, name='panorama'),
         url(r"/", IndexHandler, name='index'),
         url(r"/gui/tracking", TrackingGUIHandler, name='tracking'),
         url(r"/gui/config", ConfigGUIHandler, name='config'),
      ],
      debug=True,
      template_path = os.path.join(os.path.dirname(__file__), "templates"),
      static_path = os.path.join(os.path.dirname(__file__), "static"),
   )
   return app
