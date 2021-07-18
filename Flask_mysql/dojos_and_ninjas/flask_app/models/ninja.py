from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        if "dojo_id" in data:
            self.dojo = Dojo.dojo.get_one({"id": data['dojo_id']})
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create_ninja(cls, data):
        query = """
            INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
            VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());
        """

        ninja_id = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        print(ninja_id)
        return ninja_id


