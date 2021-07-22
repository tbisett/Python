from flask import Flask
from flask_bcrypt import Bcrypt   

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
bcrypt = Bcrypt(app) #initialize the hashing

DB = "one_to_many_practice" #create a global variable for database being accessed by models
app.secret_key = "if you have to ask, you'll never know" #create secret key for the session

