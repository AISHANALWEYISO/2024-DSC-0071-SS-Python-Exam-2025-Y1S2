from flask import Blueprint, request, jsonify
from app.models.customer import Customer
from app.status_codes import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK,HTTP_403_FORBIDDEN
from app.extensions import db

# Create a blueprint for customer
customer = Blueprint('customer', __name__, url_prefix='/api/v1/customers')


@customer.route('/create', methods=["POST"])
def createcustomer():
    try:
        
        data = request.get_json()
        name = data.get("name")
        description = data.get("description")
        category_id = data.get("category_id")
        product_id = data.get("product_id")


        
        
    #creating new customer
        new_customer = Customer(
            name=name,
            description=description,
            category_id=category_id,
            product_id=product_id,
            
        )
        
            

        # Adding the new customer instance to the database session
        db.session.add(new_customer)
        db.session.commit()

    
        return jsonify({
            'message':  customer + " has been created successfully",
            'customer': {
                "id":new_customer.id,
                'name':new_customer.name,
            'description':new_customer.description,

            }
        }), HTTP_201_CREATED

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR