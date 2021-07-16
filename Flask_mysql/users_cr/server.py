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
    return render_template("read(one).html", user = User.get_one({"id": user_id}))

@app.route("/update/<int:user_id>")
def show_update(user_id):
    return render_template("update.html", user = User.get_one({"id": user_id}))

@app.route("/users/<int:user_id>/update", methods = ['POST'])
def update_user(user_id):
    another_dict = {
        **request.form,
        "id": user_id
    }
    User.update(another_dict)
    return redirect("/")


#maybe delete post
@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    User.delete({"id": user_id})
    return redirect("/")




if __name__ == "__main__": 
    app.run(debug = True)