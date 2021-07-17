from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    #get all method is the only one that doesn't need data passed to the .query_db() method
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)
        # query results are always dictionaries
        all_dojos = []
        for row in results: 
            all_dojos.append(cls(row))
        return all_dojos

    @classmethod
    def create_dojo(cls, data):      
        query = """ 

            INSERT INTO dojos (name, created_at, updated_at)
            VALUES (%(name)s, NOW(), NOW());
        
        """

        dojo_id = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return dojo_id

    
    @classmethod
    def get_one(cls, data):
        query =  "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        #results is a list of dictionaries
        #results[0] is the dictionary at the index of 0
        dojo = cls(results[0])

        for row in results:
            row_data = {
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }

            dojo.ninjas.append(ninja.Ninja(row_data))

        return dojo

