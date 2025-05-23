from datetime import datetime
from app.extensions import db

class Customer(db.Model):
  __tablename__ = 'customers'
  id = db.Column(db.Integer ,primary_key = True )
name = db.Column(db.String(255))
description = db.Column(db.String(255))
category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
product_id = db.Column(db.Integer,db.ForeignKey('products.id'))
created_at = db.Column(db.DateTime,defult = datetime.utcnow)
updated_at = db.Column(db.DateTime, onupdate = datetime.utcnow)
category = db.relationship('Category', backref = 'customers')
product = db.relationship('Product', backref = 'customers')

def __init__(self, id, name, description):
    self.id = id
    self.name = name
    self.description = description
