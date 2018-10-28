import os

from tornado.web import url
from tornado.wsgi import WSGIApplication

from RPFirmware.handlers.gui.PanoramaHandler import PanoramaHandler
from RPFirmware.handlers.gui.TrackingHandler import TrackingHandler
from RPFirmware.handlers.gui.ConfigHandler import ConfigHandler
from RPFirmware.handlers.IndexHandler import IndexHandler


def make_app():
   app = WSGIApplication(handlers=[
         url(r"/gui/panorama", PanoramaHandler, name='panorama'),
         url(r"/", IndexHandler, name='index'),
         url(r"/gui/tracking", TrackingHandler, name='tracking'),
         url(r"/gui/config", ConfigHandler, name='config'),
      ],
      debug=True,
      template_path = os.path.join(os.path.dirname(__file__), "templates"),
      static_path = os.path.join(os.path.dirname(__file__), "static"),
   )
   return app
