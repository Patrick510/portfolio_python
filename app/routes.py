from app import app
from flask import render_template, request, jsonify
from datetime import datetime
import os

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

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

@app.route("/form01")
def form01():
  return render_template("form01.html", name="1. Personal Mini-blog", texts=texts)

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
def login02():
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
    return render_template("index.html", message=message[3], disable=False)

@app.route("/activ03")
def activ03():
    return render_template("activ03.html", name="3. Photo Upload Page")

@app.route('/sendImage', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            filename = f"{timestamp}_{file.filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            file.save(file_path)
            
            return f'File successfully uploaded! File path: {file_path}'
    
    return render_template('upload_form.html')