
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from app import app

@app.route('/')
@app.route('/index')
def index(): 
    return render_template("index.html")


@app.route('/readme/')
def readme():
    return render_template("readme.html")