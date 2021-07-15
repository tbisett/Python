from mysqlconnection import connectToMySQL

# always make class name the plural and capitalized version of the sql table name you are making a query to
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# triple quotes allow for multi-line queries
    @classmethod   
    def create(cls, data):      
        query = """ 

            INSERT INTO users (first_name, last_name, email, created_at, updated_at)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());
        
        """

        user_id = connectToMySQL("users").query_db(query, data)
        return user_id


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users").query_db(query)
        # query results are always dictionaries
        all_users = []
        for entry in results: 
            all_users.append(cls(entry))
        return all_users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("users").query_db(query, data)
        #results is a list of dictionaries
        #results[0] is the dictionary at the index of 0
        return cls(results[0])