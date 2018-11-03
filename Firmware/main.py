# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

import sys
import tornado
from tornado.options import define, options

# add your project directory to the sys.path
project_home = u'.'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from RPFirmware.app import make_app
from RPFirmware.Logger import logger


application = make_app()

define("port", default=5000, help="port to listen on")

application.listen(options.port)
logger.info("Ready : listening on port %i\n" % options.port)
tornado.ioloop.IOLoop.current().start()

