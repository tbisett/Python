from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:x>')
def four(x = 4):
    return render_template("index.html", x = x)

@app.route('/<int:x>/<int:y>')
def anyNum(x = 4, y = 4):
    return render_template("index.html", x = x, y = y)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def changeColor(x = 4, y = 4, color1 = "red", color2 = "blue"):
    return render_template("index.html", x = x, y = y, color1 = color1, color2 = color2)




if __name__ == "__main__":
    app.run(debug=True)