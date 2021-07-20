from flask import flash
from flask_bcrypt import Bcrypt
import re
from flask_app import app 
from flask_app.config.mysqlconnection import connectToMySQL
bcrypt = Bcrypt(app)

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());
        """
        user_id = connectToMySQL("login_registration").query_db(query, data)

        return user_id


    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("login_registration").query_db(query)
        
        return [cls(row) for row in results]


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("login_registration").query_db(query, data)
    
        return cls(results[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("login_registration").query_db(query, data)

        if len(results) < 1:
            return False
        
        return cls(results[0])


    @staticmethod
    def validate_user(form_data):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email format!")
            is_valid = False
        
        elif User.get_by_email({"email": form_data['email']}):
            flash("Email already exists")
            is_valid  = False

        
        if len(form_data['first_name']) <2:
            flash('First name must be at least 2 charcters')
            is_valid = False

        
        if len(form_data['last_name']) <2:
            flash('Last name must be at least 2 charcters')
            is_valid = False

        
        if len(form_data['password']) < 8:
            flash('Password name must be at least 8 charcters')
            is_valid = False
        elif form_data['password'] != form_data['confirm_password']:
            flash('Password and confirm password must match!')
            is_valid = False

        return is_valid


    @staticmethod
    def login_validate(form_data):
        user = User.get_by_email({"email": form_data['email']})
        print(user.password)
        if not user:
            flash("Invalid Email")
            return False
        
        if not bcrypt.check_password_hash(user.password, form_data['password']):
            flash("Invalid Password")
            return False
        
        return True
