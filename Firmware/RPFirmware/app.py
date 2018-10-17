from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


app = Flask(__name__)

class EmailPasswordForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    
@app.route("/", methods=['GET', 'POST'])
def hello():
   form = EmailPasswordForm()
   if form.validate_on_submit():
      print("OK")
   return render_template('index.html')
   
