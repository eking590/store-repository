
from flask_restful import Resource, reqparse 
from flask_jwt import jwt_required  
from models.item import ItemModel


class Item(Resource): 
    parser = reqparse.RequestParser() 
    parser.add_argument('price', 
        type=float, 
        required=True, 
        help="This field cannot be left blank!"
        ) 
    
    parser.add_argument('store_id', 
        type=int, 
        required=True, 
        help="Every item need a store id"
        ) 


    @jwt_required()
    def get(self, name):    #the method is a get an item from the url 
        item =  ItemModel.find_by_name(name)
        if item: 
            return item.json() 
        
        return {'message': 'item not found'}, 404  #either we return user object or we return none 

   
     
    def post(self, name):
        
        if ItemModel.find_by_name(name): #you can also use Item.find_by_name method
            return {'message': "An item with name '{}' already exit".format(name)}, 400
        
        
        data = Item.parser.parse_args() 
          
        item = ItemModel(name, **data) 
        
        try: 
            item.save_to_db() 
        except: 
            return {"message": "An error occurred when inserting the item."}, 500 


        return item.json(), 201 

    
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item: 
            item.delete_from_db() 
        
        return{'message': 'item deleted'}

        
    def put(self, name): 
        data = Item.parser.parse_args()
        
        item = ItemModel.find_by_name(name) #it can not find anything in the database 
        
        if item is None:
            item = ItemModel(name, **data) #return a new name and a price 
        else: 
            item.price = data['price']
        
        item.save_to_db()
        
        return item.json()  
    
            
class ItemList(Resource): 
    def get(self): 
        return {'items':list(map(lambda x: x.json(),ItemModel.query.all()))} 

