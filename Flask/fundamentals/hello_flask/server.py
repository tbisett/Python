from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/success')
def success():
    return "success"

@app.route('/say/<name>')
def hi(name):
    print(name)
    return "Hi, " + name + '!'

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username:" + username + ", id: " + id

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/repeat/<int:number>/<word>')
def repeat(number,word):
    return number * word

@app.route('/play')
def play():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
