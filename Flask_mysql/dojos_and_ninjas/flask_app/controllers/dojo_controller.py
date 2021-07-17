from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

# main home display route
@app.route("/")
def home():
    return render_template("index.html", all_dojos = Dojo.get_all())

@app.route("/create_dojo", methods = ['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect("/")

@app.route("/dojo_list/<int:dojo_id>")
def dojo_list(dojo_id):
    dict = {"id": dojo_id}
    return render_template("dojo_list.html", dojo = Dojo.get_one(dict))
