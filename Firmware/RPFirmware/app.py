import os

from tornado.web import url
from tornado.wsgi import WSGIApplication

from .handlers.PanoramaHandler import PanoramaHandler
from .handlers.TrackingHandler import TrackingHandler
from .handlers.ConfigHandler import ConfigHandler
from .handlers.WebsocketHandler import WSHandler
# from .Interface import setup_interface


def make_app():
   app = WSGIApplication(handlers=[
         url(r"/panorama", PanoramaHandler, name='panorama'),
         url(r"/tracking", TrackingHandler, name='tracking'),
         url(r"/config", ConfigHandler, name='config'),
         url(r'/ws', WSHandler, name='ws'),
      ],
      debug=True,
      template_path = os.path.join(os.path.dirname(__file__), "templates"),
      static_path = os.path.join(os.path.dirname(__file__), "static"),
   )
   return app
