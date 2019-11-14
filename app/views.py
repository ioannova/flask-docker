from app import app
from flask import render_template

#@app.route('/')
#def home():
#    return "Hello world!"

@app.route('/nelson')
def nelson():
    return "Olá Nelson Fonseca"

@app.route('/')
def template():
    return render_template('home.html')
