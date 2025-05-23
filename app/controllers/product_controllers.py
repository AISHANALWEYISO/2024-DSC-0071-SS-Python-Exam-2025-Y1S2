from flask import Blueprint, request ,jsonify
from app.status_codes import HTTP_400_BAD_REQUEST 
from app.models.product import Product
from app.extensions import db
#creating product blue  for product.
product = Blueprint('product', __name__, url_prefix='/api/v1/product')


@product.route('/create' , methods=['POST'])
def create_product():
    
    data = request.json
    name = data.get('name')
    price = data.get('price')
    category_id = data.get('category_id')

    
    if not name or not price:
      return jsonify({'error':'all fields are required'}),HTTP_400_BAD_REQUEST 

    new_product = Product(
    name=name ,
    price=price,
    category_id=category_id)


        

        
        db.session.add(new_product)
        db.session.commit()

        
        return jsonify({
            'message':  product + " has been created successfully",
            'product': {
                'id': new_product.id,
                'name': new_product.name,
                'price':new_product.price
            
            }
        }),  HTTP_201_CREATED

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_E