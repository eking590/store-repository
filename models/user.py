import sqlite3
from db import db 


class UserModel(db.Model): 
    __tablename__ = 'users' #tell SQLAlchemy the name of the table 

    id = db.Column(db.Integer, primary_key=True) #tell SQLAlchemy the colum of the table 
    username = db.Column(db.String(80)) #creating another column username with string size of 80 
    password = db.Column(db.String(80)) #creating another column password with string size of 80 



    def __init__(self, username, password): 
        self.username = username 
        self.password = password 
    
    def save_to_db(self): 
        db.session.add(self) 
        db.session.commit()


    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod 
    def find_by_id(cls, _id): 
        return cls.query.filter_by(id=_id).first() 