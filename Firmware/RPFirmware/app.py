import os

from tornado.web import url
from tornado.wsgi import WSGIApplication

from .handlers.PanoramaHandler import PanoramaHandler
from .handlers.TrackingHandler import TrackingHandler
from .handlers.ConfigHandler import ConfigHandler
from .handlers.IndexHandler import IndexHandler
from .handlers.WebsocketHandler import WSHandler
# from .Interface import setup_interface


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
