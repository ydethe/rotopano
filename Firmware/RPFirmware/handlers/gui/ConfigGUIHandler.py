from RPFirmware.handlers.BaseHandler import BaseHandler


class ConfigGUIHandler(BaseHandler):
    def get(self):
        self.render("config.html", **self.cfg.getDictionnary())

    def post(self):
        self.cfg.setDictionnary(self.form_to_dict())
        self.redirect("/panorama")
