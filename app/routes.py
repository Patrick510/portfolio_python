from app import app
from flask import render_template

nome = 'Patrick'

@app.route('/')
@app.route('/index')
def index():
    title = "Portfólio"
    return render_template('index.html', title=title, nome=nome)

@app.route('/contato')
def contato():
    title = "Contato"
    return render_template('contato.html', title=title, nome=nome)