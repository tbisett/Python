from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojos import Dojo


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods = ['POST'])
def submit_survey():
    if not Dojo.validate(request.form):
        return redirect ('/')
    latest_id = Dojo.submit_survey(request.form)
    return redirect(f"/results/{latest_id}")
    
    

@app.route("/results/<int:id>")
def result(id):
    print(request.form)
    dict = {"id": id}
    return render_template("results.html", dojo_id = Dojo.get_one(dict))

