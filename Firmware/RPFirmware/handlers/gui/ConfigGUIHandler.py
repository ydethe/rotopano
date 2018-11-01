from RPFirmware.handlers.BaseHandler import BaseHandler


class ConfigGUIHandler(BaseHandler):
    def get(self):
        self.render("config.html", params=list(self.cfg.getDictionnary().items()))

    def post(self):
        self.cfg.setDictionnary(self.form_to_dict())
        self.redirect("/")
