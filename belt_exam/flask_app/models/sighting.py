from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Sighting:
    def __init__(self, data):
        self.id = data['id']
        if data['user_id']:
            self.user = user.User.get_one({"id":data['user_id']})
        self.location = data['location']
        self.what_happened = data['what_happened']
        self.date_of_sighting = data['date_of_sighting']
        self.number_of_sasquatches = data['number_of_sasquatches']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_sighting(cls, data):
        print(data)
        query = """
            INSERT INTO sightings (user_id, location, what_happened, date_of_sighting, number_of_sasquatches)
            VALUES (%(user_id)s, %(location)s, %(what_happened)s, %(date_of_sighting)s, %(number_of_sasquatches)s);
        """
        # updated_at and created_at dont need to be entered because its already set as a default value in sql
        sighting_id = connectToMySQL("sasquatch_schema").query_db(query, data)
        return sighting_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sightings;"
        results = connectToMySQL("sasquatch_schema").query_db(query)
        all_sightings = []
        # for row in all_recipes:
        #     all_recipes.append(cls(row))
        # return all_recipes
        print(all_sightings)
        return [cls(row) for row in results]
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM sightings WHERE id = %(id)s;"
        results = connectToMySQL("sasquatch_schema").query_db(query, data)
    
        return cls(results[0])

    @classmethod
    def update_sighting(cls, data):
        query = """ 
            UPDATE sightings SET location= %(location)s, what_happened= %(what_happened)s, date_of_sighting = %(date_of_sighting)s, number_of_sasquatches = %(number_of_sasquatches)s
            WHERE id = %(id)s;
        
        """
        connectToMySQL("sasquatch_schema").query_db(query, data)
        # updated_at = NOW() =shouldnt need
        # id = %(id)s,
    
    @classmethod
    def delete_sighting(cls, data):
        query = "DELETE FROM sightings WHERE id = %(id)s";
        connectToMySQL("sasquatch_schema").query_db(query, data)

    @staticmethod
    def validate_sighting(form_data):
        is_valid = True
        
        if len(form_data['location']) <2:
            flash('location must be at least 2 charcters')
            is_valid = False

        
        if len(form_data['what_happened']) <2:
            flash('what happened must be at least 2 charcters')
            is_valid = False
        
        if len(form_data['date_of_sighting']) <2:
            flash('date of sighting must be at least 2 charcters')
            is_valid = False
        
        if len(form_data['number_of_sasquatches']) <1:
            flash('number of sasquatches must be at least one number')
            is_valid = False

        return is_valid