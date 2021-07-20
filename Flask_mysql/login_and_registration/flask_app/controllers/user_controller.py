from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user")
def show_user():
    return render_template("success.html", all_users = User.get_all(), user = User.get_one({"id": session['uuid']}))

@app.route("/register", methods = ["POST"])
def register():
    if not User.validate_user(request.form):
        return redirect("/")

    hash_browns = bcrypt.generate_password_hash(request.form['password'])
    dict = {
        **request.form,
        "password": hash_browns
    }

    user_id = User.create(dict)
    session["uuid"] = user_id
    return redirect("/user")

@app.route("/login", methods = ["POST"])
def login():
    if not User.login_validate(request.form):
        return redirect("/")

    user = User.get_by_email({"email": request.form['email']})
    session["uuid"] = user.id
    return redirect("/user")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

