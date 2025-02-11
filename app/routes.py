from app import app
from flask import render_template, request, jsonify
import datetime

nome = 'Patrick Dias'
attempts = {}
data = {
    "name": "admin",
    "password": "admin"
}
id_text = 0
texts = []

attempts02 = []
attempt02 = 0
message = ["Login successfully", "Login failed", "Limit attempts exceeded", "Please fill in both fields"]
validate = ["user", "admin"]

@app.route('/')
@app.route('/index')
def index():
    title = "Portfólio"
    return render_template('index.html', title=title, nome=nome)

@app.route('/activity')
def contato():
    title = "Activities"
    return render_template('activities.html', title=title, nome=nome)

@app.route('/class')
def class_page():
    title = "Classes"
    return render_template('class.html', title=title, nome=nome)

@app.route("/login")
def login():
    title = "Login page"
    return render_template("login.html", title=title)

@app.route("/auth", methods=["POST"])
def auth():
    user = request.form.get('user')
    password = request.form.get('pass')

    if user not in attempts:
        attempts[user] = 0

    if attempts[user] >= 2:
        return jsonify({"message": "Too many failed attempts. Try again later."}), 403

    if user == data['name'] and password == data["password"]:
        attempts[user] = 0
        return jsonify({"message": "Authenticated!", "user": user}), 200
    else:
        attempts[user] += 1
        return jsonify({"message": "Invalid user or password"}), 401

@app.route("/home")
def home():
  return render_template("activ01.html", name="1. Personal Mini-blog", texts=texts)

@app.route("/submit", methods=["POST"])
def submit():
  global id_text
  text = request.form.get("text")
  if text:
    id_text+=1
    date = datetime.now().strftime("%Y-%m-%d")
    texts.append({"id": id_text, "text":text, "date":date})
    message = "Texto salvo com sucesso"
  else:
    message = "Texto nao salvo"
  return render_template("form01.html", name="1. Personal Mini-blog", message=message, texts=texts)

@app.route("/activ02")
def activ02():
    return render_template("login02.html", name="2. Basic Authentication Page")

@app.route("/login02", methods=["POST"])
def login():
    global attempt02
    user = request.form.get("user")
    password = request.form.get("pass")
    
    if attempt02 == 3:
        return render_template("index02.html", message=message[2], disable=True)
    
    if user and password:
        if user == validate[0] and password == validate[1]:
            attempts02.append({"attempt": attempt02, "user": user, "date": datetime.now().strftime("%Y-%m-%d")})
            attempt02 = 0 
            return render_template("index02.html", message=message[0], disable=False)
        else:
            attempt02 += 1
            attempts02.append({"attempt": attempt02, "user": user, "date": datetime.now().strftime("%Y-%m-%d")})
            return render_template("index02.html", message=message[1])

    attempt02 = 0
    return render_template("index02.html", message=message[3], disable=False)