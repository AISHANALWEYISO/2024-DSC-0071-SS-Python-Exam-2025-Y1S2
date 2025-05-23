from flask import Blueprint, request ,jsonify
from app.status_codes import HTTP_400_BAD_REQUEST ,HTTP_201_CREATED ,HTTP_500_INTERNAL_SERVER_ERROR
from app.models.category import Category
from app.extensions import db

#creating product blue  for category.
category = Blueprint('category', __name__, url_prefix='/api/v1/category')

@category.route('/create' , methods=['POST'])
def create_category():
    
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({'error':'all fields are required'}),HTTP_400_BAD_REQUEST
    
    try:
         new_category = Category(name=name)
         db.session.add(new_category)
         db.session.commit()

         categoryname = new_category.get_full_name()
    
    return({
        'message': categoryname + "has been created",
        'category':{
            'id':new_category.id,
            'name':new_category.name
        }
    }), HTTP_201_CREATED

    except Exception as e:
        db.session.rollback()
        return jsonify ({"error":str(e)}),HTTP_500_INTERNAL_SERVER_ERROR
