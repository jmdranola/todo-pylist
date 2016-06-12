
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from app import app

@app.route('/')
@app.route('/index')
def index(): 
    return "Hello, World!!"

@app.route('/templates/')
def templates():
    return render_template("index.html")