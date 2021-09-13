import sqlite3 
from flask_restful import Resource, reqparse
from models.user import UserModel 


class UserRegister(Resource): 
    
    parser = reqparse.RequestParser() 
    parser.add_argument('username', 
        type=str, 
        required=True, 
        help="please Insert you username!"
        ) 
    
    parser.add_argument('password', 
        type=str, 
        required=True, 
        help="please this field cannot be left blank"
        ) 
    
    
    def post(self): 
        data = UserRegister.parser.parse_args()    #got the data from the JSON payload and his flask RESTFUL 
        if UserModel.find_by_username(data['username']): #preventing duplicate usernames when signing users 
            return {'message': 'this user already exist '}, 400 

        user = UserModel(**data) 
        user.save_to_db()

        return {'message':'User created successfully'}, 201 

        