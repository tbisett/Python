from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route("/recipes/<int:recipe_id>")
def display_recipe(recipe_id):
    if "uuid" not in session:
        return redirect("/")
    dict = {"id":recipe_id}
    dict1 = {"id":session['uuid']}
    return render_template("instructions.html",  recipe = Recipe.get_one(dict), user = User.get_one(dict1))

@app.route("/recipes/new")
def new_recipe():
    if "uuid" not in session:
        return redirect("/")
    return render_template("new_recipe.html")

@app.route("/create/recipe", methods = ['POST'])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect("/recipes/new")
    form_data = {
        **request.form,
        "user_id": session['uuid']
    }
    Recipe.create_recipe(form_data)
    return redirect ("/user/dashboard")

@app.route("/recipes/edit/<int:recipe_id>")
def edit_recipe_page(recipe_id):
    if "uuid" not in session:
        return redirect("/")
    dict = {"id":recipe_id}
    return render_template("edit_recipe.html", recipe = Recipe.get_one(dict))

@app.route("/edit/recipe/<int:id>", methods = ['POST'])
def edit_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect("/recipes/edit/<int:recipe_id>")
    Recipe.update_recipe(request.form)
    return redirect("/user/dashboard")

@app.route("/delete/recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    if "uuid" not in session:
        return redirect("/")
    dict = {"id":recipe_id}
    Recipe.delete_recipe(dict)
    return redirect("/user/dashboard")


