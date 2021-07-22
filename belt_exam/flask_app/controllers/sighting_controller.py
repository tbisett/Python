from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.sighting import Sighting
from flask_app.models.user import User
# <int:sighting_id> may have to be sightings
#app route displays single sighting

@app.route("/show/<int:sighting_id>")
def display_sighting(sighting_id):
    if "uuid" not in session:
        return redirect("/")
    dict = {"id":sighting_id}
    dict1 = {"id":session['uuid']}
    return render_template("show.html", sighting = Sighting.get_one(dict), user = User.get_one(dict1))

# app route renders new sighting page

@app.route("/sighting/new")
def new_sighting():
    if "uuid" not in session:
        return redirect("/")
    dict = {"id": session['uuid']}
    return render_template("new_sighting.html", user = User.get_one(dict) )

# app route is the post method for new sightings page

@app.route("/create/sighting", methods = ['POST'])
def create_sighting():
    if not Sighting.validate_sighting(request.form):
        return redirect("/sighting/new")
    form_data = {
        **request.form,
        "user_id": session['uuid']
    }
    Sighting.create_sighting(form_data)
    return redirect ("/user/dashboard")

# app route is edit sighting render page

@app.route("/edit/<int:sighting_id>")
def edit_sighting_page(sighting_id):
    if "uuid" not in session:
        return redirect("/")
    dict = {"id":sighting_id}
    dict1 = {"id": session['uuid']}
    return render_template("edit_sighting.html", sighting = Sighting.get_one(dict), user = User.get_one(dict1))

# app route is post method for edit sighting page
# may have to change <int:id> to <int:sighting_id>
# may have to input sighting_id into edit_sighting() as parameter

@app.route("/edit/sighting/<int:id>", methods = ['POST'])
def edit_sighting(id):
    if not Sighting.validate_sighting(request.form):
        return redirect(f"/edit/{id}")

    form_data = {
       **request.form,
        "id":id
    }

    Sighting.update_sighting(form_data)
    return redirect("/user/dashboard")

# app route is delete method for sightings

@app.route("/delete/sighting/<int:sighting_id>")
def delete_recipe(sighting_id):
    if "uuid" not in session:
        return redirect("/")
    dict = {"id":sighting_id}
    Sighting.delete_sighting(dict)
    return redirect("/user/dashboard")


