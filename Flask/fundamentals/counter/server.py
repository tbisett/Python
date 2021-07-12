from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = "super secret secure key"

@app.route("/")
def index():
    session['counter'] += 1
    return render_template("index.html")

@app.route("/destroy_session")
def DestroySession():
    session.clear()
    session['counter'] = 0
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)