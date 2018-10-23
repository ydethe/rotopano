import os

from tornado.web import Application, RequestHandler, url

from .handlers import PanoramaHandler, TrackingHandler, ConfigHandler
# from .Interface import setup_interface


# class PanoramaHandler(RequestHandler):
   # def get(self):
      # from .Config import Config
      # cfg = Config()
      # self.render("panorama.html", pano_modes=['Photo', 'Horizontal panorama', 'Half sphere panorama'], **cfg.getDictionnary())


def make_app():
   app = Application(handlers=[
         url(r"/panorama", PanoramaHandler, name='panorama'),
         url(r"/tracking", TrackingHandler, name='tracking'),
         url(r"/config", ConfigHandler, name='config'),
      ],
      debug=True,
      template_path = os.path.join(os.path.dirname(__file__), "templates"),
      static_path = os.path.join(os.path.dirname(__file__), "static"),
   )
   return app
   
# def handle_client_connect_event(json):
   # print('received json: {0}'.format(str(json)))
   
# def handle_json_button(json):
   # # it will forward the json to all clients.
   # print('progress json: {0}'.format(str(json)))
   # json = json.jsonify({'progress':40})
   # send(json, json=True)
   
# @app.route("/")
# def default():
   # return redirect('/panorama')
   
# @app.route("/panorama", methods=['GET', 'POST'])
# def panorama():
   # cfg = Config()
   # if request.method == "POST":
      # cfg.setDictionnary(request.form)
      # print(cfg)
      
   # return render_template('panorama.html', pano_modes=['Photo','Horizontal panorama', 'Half sphere panorama'], **cfg.getDictionnary())
   
# @app.route("/_pano_update")
# def panorama_update():
   # cfg = Config()
   # return json.jsonify({'progress':40})
   
# @app.route("/tracking", methods=['GET', 'POST'])
# def tracking():
   # cfg = Config()
   # if request.method == "POST":
      # cfg.setDictionnary(request.form)
      # eph = RPEphemeris()
      # bdy = eph.getBody(cfg.getParam('trk_body'))
      # alt, az, d = eph.getAltAz(bdy, EarthLocation(lat=48.829456*u.deg, lon=2.302180*u.deg, height=0*u.m))
      # print("%s : Alt=%.1fdeg, az=%.1fdeg, d=%.1fkm" % (cfg.getParam('trk_body'), alt*180/np.pi,az*180/np.pi,d/1000))
      
   # return render_template('tracking.html', bodies=RPEphemeris.listBodies(), **cfg.getDictionnary())

# @app.route("/config", methods=['GET', 'POST'])
# def config():
   # cfg = Config()
   # if request.method == "POST":
      # cfg.setDictionnary(request.form)
      # print(cfg)
      
      # return redirect('/')
      
   # return render_template('config.html', **cfg.getDictionnary())
   
   
   