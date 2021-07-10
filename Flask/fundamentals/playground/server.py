from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/play')
def play():
    return render_template("index.html")

@app.route('/play/<int:n>')
@app.route('/play/<int:n>/<string:color>')
def box_color(n = 4, color = "blue"):
    return render_template('index.html', n = n, color = color)


if __name__ == "__main__":
    app.run(debug=True)