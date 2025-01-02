from app import app
from flask import render_template, request, jsonify

nome = 'Patrick Dias'
attempts = {}
data = {
    "name": "admin",
    "password": "admin"
}

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