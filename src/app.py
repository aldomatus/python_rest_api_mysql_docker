# Flask libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Third-party libraries
from sqlalchemy import ForeignKey
from datetime import datetime

# For seed script
import csv

#-------------------database connection------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


#----------------Models-------------------------------
# Address information model
class RemitentAddress(db.Model):
    __tablename__= 'remitentaddress'
    id = db.Column(db.Integer, primary_key=True)
    postal_code = db.Column(db.String(10))
    state = db.Column(db.String(30), unique=False)
    municipality = db.Column(db.String(100), unique=False)
    city = db.Column(db.String(100), unique=False)
    colony = db.Column(db.String(100), unique=False)

    remitent_id = db.Column(db.Integer, db.ForeignKey('remitent.id'))

    def __init__(self, postal_code, state, municipality, city, colony):
        self.postal_code = postal_code
        self.state = state
        self.municipality = municipality
        self.city = city
        self.colony = colony

class RemitentAddressSchema(ma.Schema):
    class Meta:
      fields = ("id", "postal_code", "state", "municipality", "city", "colony", "remitent_id")

address_r_schema = RemitentAddressSchema()
addresses_r_schema = RemitentAddressSchema(many=True)


# Address information model
class DestinataryAddress(db.Model):
    __tablename__= 'destinataryaddress'
    id = db.Column(db.Integer, primary_key=True)
    postal_code = db.Column(db.String(10))
    state = db.Column(db.String(30), unique=False)
    municipality = db.Column(db.String(100), unique=False)
    city = db.Column(db.String(100), unique=False)
    colony = db.Column(db.String(100), unique=False)

    remitent_id = db.Column(db.Integer, db.ForeignKey('destinatary.id'))

    def __init__(self, postal_code, state, municipality, city, colony):
        self.postal_code = postal_code
        self.state = state
        self.municipality = municipality
        self.city = city
        self.colony = colony

class DestinataryAddressSchema(ma.Schema):
    class Meta:
      fields = ("id", "postal_code", "state", "municipality", "city", "colony", "remitent_id")

address_d_schema = DestinataryAddressSchema()
addresses_d_schema = DestinataryAddressSchema(many=True)

# Shipping information model
class Shipping(db.Model):
    __tablename__= 'shipping'
    id = db.Column(db.Integer, primary_key=True)
    contents = db.Column(db.String(100), nullable=False, unique=False)
    product_value = db.Column(db.Float)
    description = db.Column(db.String(100))
    delivered = db.Column(db.Boolean, default=0)
    shipping_price = db.Column(db.Float, nullable=False)
    shipping_date = db.Column(db.DateTime)
    
    remitent_id = db.Column(db.Integer, db.ForeignKey('remitent.id'))
    destinatary_id = db.Column(db.Integer, db.ForeignKey('destinatary.id'))

    def __init__(self, contents, product_value, description, delivered, shipping_price, shipping_date):
        self.contents = contents
        self.product_value = product_value
        self.description = description
        self.delivered = delivered
        self.shipping_price = shipping_price
        self.shipping_date = shipping_date

class ShippingSchema(ma.Schema):
    class Meta:
        ields = ("id", "contents", "product_value", "description", "delivered", "shipping_price", "shipping_date", "remitent_id", "destinatary_id")

shipping_schema = ShippingSchema()
shippings_schema = ShippingSchema(many=True)
    

# Remitent information model
class Remitent(db.Model):
    __tablename__= 'remitent'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)

    shippings = db.relationship('Shipping')
    address = db.relationship('RemitentAddress')

    def __init__(self, name, last_name, phone):
        self.name = name
        self.last_name = last_name
        self.phone = phone

class RemitentSchema(ma.Schema):
    class Meta:
      fields = ("id", "name", "last_name", "phone")

remitent_schema = RemitentSchema()
remitents_schema = RemitentSchema(many=True)        


# Destinatary information model
class Destinatary(db.Model):
    __tablename__= 'destinatary'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    last_name = db.Column(db.String(100), unique=False)
    address_model_d = db.Column(db.String(100))
    phone = db.Column(db.String(20), unique=False)
    postal_code = db.Column(db.String(10))
    
    remitent_id = db.relationship('Shipping')
    address = db.relationship('DestinataryAddress')

    def __init__(self, name, last_name, address_model_d, phone, postal_code):
        
        self.name = name
        self.last_name = last_name
        self.address_model_d = address_model_d
        self.phone = phone
        self.postal_code = postal_code

class DestinatarySchema(ma.Schema):
    class Meta:
       fields = ("id", "name", "last_name", "address_model_d", "phone", "postal_code")

destinatary_schema = DestinatarySchema()
destinataries_schema = DestinatarySchema(many=True)  


# Address information model
class Address(db.Model):
    __tablename__= 'address'
    id = db.Column(db.Integer, primary_key=True)
    postal_code = db.Column(db.String(10))
    state = db.Column(db.String(30), unique=False)
    municipality = db.Column(db.String(100), unique=False)
    city = db.Column(db.String(100), unique=False)
    colony = db.Column(db.String(100), unique=False)

    def __init__(self, postal_code, state, municipality, city, colony):
        self.postal_code = postal_code
        self.state = state
        self.municipality = municipality
        self.city = city
        self.colony = colony
db.create_all()
class AddressSchema(ma.Schema):
    class Meta:
      fields = ("id", "postal_code", "state", "municipality", "city", "colony")

address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)


#-----------------Upload the SEPOMEX files to the database---------------
# Seed script
def import_data(file):
    """
    Seed script to import SEPOMEX data to MySQL database
    """
    with open(str(file)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_counter = 0
        for row in csv_reader:
            if line_counter != 0:
                postal_code=row[0]
                colony=row[1]
                municipality=row[3],
                state=row[4]
                city=row[5]
                
                new_address= Address(postal_code, state, municipality, city, colony)
                db.session.add(new_address)
                db.session.commit()
            line_counter += 1

import_data('puebla.csv')

#----------------REST APIS---------------------------
# Welcome to Cura Deuda ® API
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to Cura Deuda ® API'})

# To create news addresses
@app.route('/address', methods=['POST'])
def create_address():
    # Receive requests
    if request.method == 'POST':
        postal_code = request.json['postal_code']
        state = request.json['state']
        municipality = request.json['municipality']
        city = request.json['city']
        colony = request.json['colony']

        new_address= RemitentAddress(postal_code, state, municipality, city, colony)

        db.session.add(new_address)
        db.session.commit()

        return address_schema.jsonify(new_address)


# Save a customer submission service to the database
@app.route('/shippings', methods=['POST'])
def create_shipping():

    # Receive requests
    if request.method == 'POST':

        # shipping information
        contents = request.json['contents']
        product_value = request.json['product_value']
        description = request.json['description']
        delivered = request.json['delivered']
        shipping_price = request.json['shipping_price']
        shipping_date = datetime.today()

        new_shipping= Shipping(contents, product_value, description, delivered, shipping_price, shipping_date)
        db.session.add(new_shipping)
        

        # Remitent information
        name_r = request.json['name_r']
        last_name_r = request.json['last_name_r']
        phone_r = request.json['phone_r']

        postal_code_r = request.json['postal_code_r']
        state_r = request.json['state_r']
        municipality_r = request.json['municipality_r']
        city_r = request.json['city_r']
        colony_r = request.json['colony_r']

        new_address_r= RemitentAddress(postal_code_r, state_r, municipality_r, city_r, colony_r)
        db.session.add(new_address_r)

        new_remitent = Remitent(name_r, last_name_r, phone_r)
        db.session.add(new_remitent)

        # Destinatary information
        name_d = request.json['name_d']
        last_name_d = request.json['last_name_d']
        address_model_d = request.json['address_model_d']
        phone_d = request.json['phone_d']
        postal_code_d = request.json['postal_code_d']

        postal_code_d = request.json['postal_code_d']
        state_d = request.json['state_d']
        municipality_d = request.json['municipality_d']
        city_d = request.json['city_d']
        colony_d = request.json['colony_d']
        
        new_address_d= DestinataryAddress(postal_code_d, state_d, municipality_d, city_d, colony_d)
        db.session.add(new_address_d)

        new_destinatary= Destinatary(name_d, last_name_d, address_model_d, phone_d, postal_code_d)
        db.session.add(new_destinatary)

        db.session.commit()
        return destinatary_schema.jsonify(new_destinatary)


    return jsonify({'message': 'Data stored successfully!'})


# Search for colonies by zip code
@app.route('/address/cp/<string:postal_code>', methods=['GET'])
def get_colonies(postal_code):
    colonies = Address.query.filter_by(postal_code=postal_code).all()
    result = addresses_schema.dump(colonies)
    return jsonify(result)

# search for colonies, municipalities and states by name
@app.route('/address/colonies/<string:place>', methods=['GET'])
def get_colonies_name(place):
    colonies = Address.query.filter_by(colony=place).all()
    result = addresses_schema.dump(colonies)
    return jsonify(result)

# search for municipalities by name
@app.route('/address/municipalities/<string:place>', methods=['GET'])
def get_municipalities_name(place):
    municipalities = Address.query.filter_by(municipality=place).all()
    result = addresses_schema.dump(municipalities)
    return jsonify(result)

# search for states by name
@app.route('/address/state/<string:place>', methods=['GET'])
def get_state_name(place):
    states = Address.query.filter_by(state=place).all()
    result = addresses_schema.dump(states)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
