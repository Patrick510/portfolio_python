from app import app
from flask import render_template

nome = 'Patrick Dias'

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