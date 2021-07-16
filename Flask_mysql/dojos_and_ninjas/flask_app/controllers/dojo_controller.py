from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

# main home display route
@app.route("/")
def home():
    return render_template("index.html")

#  new ninja display route

@app.route("/new_ninja")
def new_ninja():
    return render_template("new_ninja.html")