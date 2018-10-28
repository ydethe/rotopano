from RPFirmware.handlers.BaseHandler import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        self.redirect("/gui/panorama")
