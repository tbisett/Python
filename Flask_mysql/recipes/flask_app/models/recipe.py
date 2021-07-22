from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        if data['user_id']:
            self.user = user.User.get_one({"id":data['user_id']})
        self.name = data['name']
        self.description = data['description']
        self.under_30_minutes = data['under_30_minutes']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_recipe(cls, data):
        print(data)
        query = """
            INSERT INTO recipes (user_id, name, description, under_30_minutes, instructions, date_made, created_at, updated_at)
            VALUES (%(user_id)s, %(name)s, %(description)s, %(under_30_minutes)s, %(instructions)s, %(date_made)s, NOW(), NOW());
        """
        recipe_id = connectToMySQL("recipes").query_db(query, data)
        return recipe_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL("recipes").query_db(query)
        all_recipes = []
        # for row in all_recipes:
        #     all_recipes.append(cls(row))
        # return all_recipes
        print(all_recipes)
        return [cls(row) for row in results]
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL("recipes").query_db(query, data)
    
        return cls(results[0])

    @classmethod
    def update_recipe(cls, data):
        query = """ 
            UPDATE recipes SET id = %(id)s, name= %(name)s, description = %(description)s, under_30_minutes = %(under_30_minutes)s, instructions = %(instructions)s, date_made = %(date_made)s,
            updated_at = NOW() WHERE id = %(id)s;
        
        """
        connectToMySQL("recipes").query_db(query, data)
    
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s";
        connectToMySQL("recipes").query_db(query, data)

    @staticmethod
    def validate_recipe(form_data):
        is_valid = True
        
        if len(form_data['name']) <3:
            flash('Name must be at least 3 charcters')
            is_valid = False

        
        if len(form_data['description']) <3:
            flash('Description must be at least 3 charcters')
            is_valid = False
        
        if len(form_data['instructions']) <3:
            flash('Instructions must be at least 3 charcters')
            is_valid = False