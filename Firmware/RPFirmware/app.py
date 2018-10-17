from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route("/")
@app.route("/control")
def control():
   if 'action' in request.args.keys():
      print("action : %s" % (request.args['action']))
      
   return render_template('index.html')

@app.route("/config", methods=['GET', 'POST'])
def config():
   if request.method == "POST":
      for key in request.form.keys():
         for value in request.form.getlist(key):
            print(key,":",value)
      return redirect('/control')
      
   return render_template('config.html')
   