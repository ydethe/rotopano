# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

import sys
import tornado

# add your project directory to the sys.path
project_home = u'.'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from RPFirmware.app import make_app


application = make_app()

application.listen(5000)
print("Ready : listening on port 5000")
tornado.ioloop.IOLoop.current().start()

