from flask import Flask
from flask import render_template

xapp = Flask(__name__)

@xapp.route("/")
def start():
  return render_template("activity04.html")

@xapp.route("/activity01")
def activity01():
  return render_template("activity01.html") 

@xapp.route("/activity02")
def activity02():
  return render_template("activity02.html") 

@xapp.route("/activity03")
def activity03():
  return render_template("activity03.html") 

@xapp.route("/activity04")
def activity04():
  return render_template("activity04.html") 

@xapp.route("/curriculum01")
def curriculum01():
  return render_template("curriculum01.html") 

@xapp.route("/curriculum02")
def curriculum02():
  return render_template("curriculum02.html") 

@xapp.route("/curriculum03")
def curriculum03():
  return render_template("curriculum03.html") 

@xapp.route("/curriculum04")
def curriculum04():
  return render_template("curriculum04.html") 

@xapp.route("/curriculum05")
def curriculum05():
  return render_template("curriculum05.html") 

@xapp.route("/curriculum06")
def curriculum06():
  return render_template("curriculum06.html") 

@xapp.route("/contact")
def contact():
  return render_template("contact.html") 

if __name__ == "__main__":
  xapp.run(debug=True, host="0.0.0.0")