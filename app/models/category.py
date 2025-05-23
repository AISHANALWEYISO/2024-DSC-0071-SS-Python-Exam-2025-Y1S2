from app.extensions import db
from datetime import datetime

#creating the category model
class Category(db.Model):
    __tablename__ = 'categories'
id = db.Column(db.integer ,primary_key = True )
name = db.Column(db.String(255))
created_at = db.Column(db.DateTime,defult = datetime.utcnow)
updated_at = db.Column(db.DateTime, onupdate = datetime.utcnow)

def __init__(self, id, name):
    self.id = id
    self.name = name
    