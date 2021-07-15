from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)
app.secret_key = "keep it simple, keep it safe"

@app.route("/")
def index():
    return render_template("read(all).html", all_users = User.get_all())

@app.route("/register_user")
def register():
    return render_template("create.html")

@app.route("/create_user", methods = ['POST'])
def create():
    User.create(request.form)
    return redirect("/")

@app.route("/users/<int:user_id>")
def display_user(user_id):
    return render_template("read_all.html", user = User.get_one({"id": user_id}))







if __name__ == "__main__": 
    app.run(debug = True)