from flask import Flask, render_template, request, redirect
from astropy.coordinates import EarthLocation
import astropy.units as u
import numpy as np

from .Config import Config
from .Interface import setup_interface
from .RPEphemeris import RPEphemeris


app = Flask(__name__)
app.tache = setup_interface()
app.tache.start()

@app.route("/")
def default():
   return redirect('/panorama')
   
@app.route("/panorama", methods=['GET', 'POST'])
def panorama():
   cfg = Config()
   if request.method == "POST":
      cfg.setDictionnary(request.form)
      print(cfg)
      
   return render_template('panorama.html', pano_modes=['Photo','Horizontal panorama', 'Half sphere panorama'], **cfg.getDictionnary())
   
@app.route("/tracking", methods=['GET', 'POST'])
def tracking():
   cfg = Config()
   if request.method == "POST":
      cfg.setDictionnary(request.form)
      eph = RPEphemeris()
      bdy = eph.getBody(cfg.getParam('trk_body'))
      alt, az, d = eph.getAltAz(bdy, EarthLocation(lat=48.829456*u.deg, lon=2.302180*u.deg, height=0*u.m))
      print("%s : Alt=%.1fdeg, az=%.1fdeg, d=%.1fkm" % (cfg.getParam('trk_body'), alt*180/np.pi,az*180/np.pi,d/1000))
      
   return render_template('tracking.html', bodies=RPEphemeris.listBodies(), **cfg.getDictionnary())

@app.route("/config", methods=['GET', 'POST'])
def config():
   cfg = Config()
   if request.method == "POST":
      cfg.setDictionnary(request.form)
      print(cfg)
      
      return redirect('/')
      
   return render_template('config.html', **cfg.getDictionnary())
   
   
   