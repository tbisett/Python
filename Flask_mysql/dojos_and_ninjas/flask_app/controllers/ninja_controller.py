from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route("/new_ninja")
def new_ninja():
    return render_template("new_ninja.html")

@app.route("/create_ninja", methods = ['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return render_template("index.html", all_dojos = Dojo.get_all())