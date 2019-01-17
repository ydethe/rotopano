from RPFirmware.handlers.BaseHandler import BaseHandler
from RPFirmware.ActionManager import ActionManager


class LoggerGUIHandler(BaseHandler):
    def get(self):
        self.render("logger.html")
        