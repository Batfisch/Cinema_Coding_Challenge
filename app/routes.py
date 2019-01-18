from app import app
from flask import render_template, flash, redirect, url_for, request


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    time = [12,2,13]
    return render_template("index.html", time=time)
