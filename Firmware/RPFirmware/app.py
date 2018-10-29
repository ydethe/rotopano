import os

from tornado.web import url
from tornado.wsgi import WSGIApplication

<<<<<<< .mine
from RPFirmware.handlers.gui.PanoramaGUIHandler import PanoramaGUIHandler
from RPFirmware.handlers.gui.TrackingGUIHandler import TrackingGUIHandler
from RPFirmware.handlers.gui.ConfigGUIHandler import ConfigGUIHandler
from RPFirmware.handlers.state.PanoramaStateHandler import PanoramaStateHandler
=======
from RPFirmware.handlers.gui.PanoramaGUIHandler import PanoramaGUIHandler
from RPFirmware.handlers.gui.TrackingGUIHandler import TrackingGUIHandler
from RPFirmware.handlers.gui.ConfigGUIHandler import ConfigGUIHandler
>>>>>>> .r61
from RPFirmware.handlers.IndexHandler import IndexHandler


def make_app():
   app = WSGIApplication(handlers=[
<<<<<<< .mine
         url(r"/gui/panorama", PanoramaGUIHandler, name='/gui/panorama'),
         url(r"/", IndexHandler, name='/index'),
         url(r"/gui/tracking", TrackingGUIHandler, name='/gui/tracking'),
         url(r"/gui/config", ConfigGUIHandler, name='/gui/config'),
         url(r"/state/panorama", PanoramaStateHandler, name='/state/panorama'),
=======
         url(r"/gui/panorama", PanoramaGUIHandler, name='panorama'),
         url(r"/", IndexHandler, name='index'),
         url(r"/gui/tracking", TrackingGUIHandler, name='tracking'),
         url(r"/gui/config", ConfigGUIHandler, name='config'),
>>>>>>> .r61
      ],
      debug=True,
      template_path = os.path.join(os.path.dirname(__file__), "templates"),
      static_path = os.path.join(os.path.dirname(__file__), "static"),
   )
   return app
