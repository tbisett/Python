from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data ['updated_at']


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s"
        results = connectToMySQL("dojo_survey").query_db(query, data)

        dojo = cls(results[0])

        return dojo


    @classmethod
    def submit_survey(cls, data):      
        query = """ 

            INSERT INTO dojos (name, location, language, comment, created_at, updated_at)
            VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());
        
        """

        submit_survey_id = connectToMySQL("dojo_survey").query_db(query, data)
        print(submit_survey_id)
        return submit_survey_id

    @staticmethod
    def validate(post_data):
        # the purpose of this function is to return True or False
        # post_data: this is the data from request.form
            # post_data is a dictionary: the keys are the form input fields
        is_valid = True # we start with assuming the data is valid

        # we use if statements to check the data
        # if the data isn't valid, we set is_valid = False
        ### the data we get from the form is all strings
        
        if len(post_data['name']) < 3:
            # flash messages exist for just one HTTP req/res cycle
            flash("Name must be at least 3 characters.")
            is_valid = False
        
        if len(post_data['location']) < 3:
            flash("Name must be submitted")
            is_valid = False
    
        
        
        if len(post_data['language']) < 3:
            flash("Dog hair color must be at least 3 characters")
            is_valid = False

        if len(post_data['comment']) < 2:
            flash("Your comment must be longer that 3 characters")
            is_valid = False

        return is_valid
