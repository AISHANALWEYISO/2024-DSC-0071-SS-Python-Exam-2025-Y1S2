from datetime import datetime
from app.extensions import db

#creating a product 
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer ,primary_key = True )
name = db.Column(db.String(255))
price = db.Column(db.String(255))
category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
created_at = db.Column(db.DateTime,defult = datetime.utcnow)
updated_at = db.Column(db.DateTime, onupdate = datetime.utcnow)
category = db.relationship('Category', backref = 'products')

def __init__(self, id, name, price):
    self.id = id
    self.name = name
    self.price = price