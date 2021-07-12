from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "super secret safe password"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods = ['POST'])
def result():
    print("info received")
    print (request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/display") 

@app.route("/display")
def display():
    print(request.form)
    return render_template("display.html")





if __name__ == "__main__":
    app.run(debug = True)