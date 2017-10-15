from flask import render_template
from . import main

@main.route('/')
def index():
    print "OK"
    return render_template("index.html")