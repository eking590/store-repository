 
from flask import Flask  
from flask_restful import Resource, Api   
from flask_jwt import JWT  
from security import authenticate, identity 
import os
from resources.user import UserRegister
from resources.item import Item, ItemList 
from resources.store import Store, StoreList 


app = Flask(__name__) 
app.secret_key = 'ebor' 
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///data.db') #the sqlite database will be situated at the root folder of our project 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #To off flask sql alchemy behaviour while activating the usual SQLAlchemy modifications 
api = Api(app)  #finding our api 



@app.before_first_request
def create_tables(): 
    db.create_all() 


jwt = JWT(app, authenticate, identity) #/auth 

#defining your  the method the resource is going to accept 

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>') 
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreList, '/store')


from db import db    
db.init_app(app)


if __name__ == '__main__': 
    app.run(port=5000, debug=True)





