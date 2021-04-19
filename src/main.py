"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Favorites
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager
# from models import Person
# import JWT for tokenization
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    get_jwt_identity,
    create_access_token,
)
# Server creation with Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_CONNECTION_STRING")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
jwt = JWTManager(app)
# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code
# generate sitemap with all your endpoints
@app.route("/")
def sitemap():
    return generate_sitemap(app)

@app.route("/user", methods=["GET"])
def handle_hello():
    response_body = {"msg": "Hello, this is your GET /user response "}
    return jsonify(response_body), 200
    
# register endpoint
@app.route("/register", methods=["POST"])
def register_user():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    # validation of possible empty inputs
    if email is None:
        return jsonify({"msg": "No email was provided"}), 400
    if password is None:
        return jsonify({"msg": "No password was provided"}), 400
    # busca usuario en BBDD
    user = User.query.filter_by(email=email).first()
    if user:
        # the user was not found on the database
        return jsonify({"msg": "User already exists"}), 401
    else:
        # crea nuevo usuario
        new_user = User()
        new_user.email = email
        new_user.password = password
        # crea registro nuevo en BBDD de
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 200

@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    # valida si estan vacios los ingresos
    if email is None:
        return jsonify({"msg": "No email was provided"}), 400
    if password is None:
        return jsonify({"msg": "No password was provided"}), 400
    # para proteger contraseñas usen hashed_password
    # busca usuario en BBDD
    user = User.query.filter_by(email=email, password=password).first()
    if user is None:
        return jsonify({"msg": "Invalid username or password"}), 401
    else:
        # crear token
        my_token = create_access_token(identity=user.id)
        return jsonify({"token": my_token})
# PORQUE CARAJOS PROTECTED TIENE DOBLE COMILLAS Y EL RESTO, COMILLA SENCILLA
@app.route("/protected", methods=["GET", "POST"])
# protege ruta con esta funcion
@jwt_required()
def protected():
    # busca la identidad del token
    current_id = get_jwt_identity()
    # busca usuarios en base de datos
    user = User.query.get(current_id)
    print(user)
    return jsonify({"id": user.id, "email": user.email}), 200

# add peoples endpoint
@app.route("/people", methods=["POST"])
def add_people():
    name = request.json.get("name", None)
    birth_year = request.json.get("birth_year", None)
    gender = request.json.get("gender", None)
    height = request.json.get("height", None)
    skin_color = request.json.get("skin_color", None)
    hair_color = request.json.get("hair_color", None)
    eye_color = request.json.get("eye_color", None)
    # validation of possible empty inputs
    if name is None:
        return jsonify({"msg": "No name was provided"}), 400
    if birth_year is None:
        return jsonify({"msg": "No birth year was provided"}), 400
    if gender is None:
        return jsonify({"msg": "No gender was provided"}), 400
    if height is None:
        return jsonify({"msg": "No height was provided"}), 400
    if skin_color is None:
        return jsonify({"msg": "No skin color was provided"}), 400
    if hair_color is None:
        return jsonify({"msg": "No hair color was provided"}), 400
    if eye_color is None:
        return jsonify({"msg": "No eye color was provided"}), 400
    # busca people en BBDD
    people = people.query.filter_by(name=name).first()
    if people:
        # the  was found on the database
        return jsonify({"msg": "people already exists"}), 401
    else:
        new_people = people()
        new_people.name = name
        new_people.birth_year = birth_year
        new_people.gender = gender
        new_people.height = height
        new_people.skin_color = skin_color
        new_people.hair_color = hair_color
        new_people.eye_color = eye_color
        db.session.add(new_people)
        db.session.commit()
        return jsonify({"msg": "people created successfully"}), 200

@app.route("/people", methods=["GET"])
def get_characters():
    allpeople = People.query.all()
    allpeople = list(map(lambda x: x.serialize(),allpeople))
    return jsonify(allpeople), 200

app.route("/planets", methods=["POST"])
def add_planets():
    name = request.json.get("name", None)
    climate = request.json.get("climate", None)
    population = request.json.get("population", None)
    orbital_period = request.json.get("orbital_period", None)
    rotation_period = request.json.get("rotation_period", None)
    diameter = request.json.get("diameter", None)
    terrain = request.json.get("terrain", None)
    # validation of possible empty inputs
    if name is None:
        return jsonify({"msg": "No name was provided"}), 400
    if climate is None:
        return jsonify({"msg": "No climate was provided"}), 400
    if population is None:
        return jsonify({"msg": "No population was provided"}), 400
    if orbital_period is None:
        return jsonify({"msg": "No orbital_period was provided"}), 400
    if rotation_period is None:
        return jsonify({"msg": "No rotation_period was provided"}), 400
    if diameter is None:
        return jsonify({"msg": "No diameter was provided"}), 400
    if terrain is None:
        return jsonify({"msg": "No terrain was provided"}), 400
    # busca character en BBDD
    planet = Planets.query.filter_by(name=name).first()
    if planet:
        # the planet was found on the database
        return jsonify({"msg": "Planet already exists"}), 401
    else:
        new_planet = Planets()
        new_planet.name = name
        new_planet.climate = climate
        new_planet.population = population
        new_planet.orbital_period = orbital_period
        new_planet.rotation_period = rotation_period
        new_planet.diameter = diameter
        new_planet.terrain = terrain
        db.session.add(new_planet)
        db.session.commit()
        return jsonify({"msg": "Planet created successfully"}), 200    

@app.route("/planets", methods=["GET"])
def get_planets():
    allplanets = Planets.query.all()
    allplanets = list(map(lambda x: x.serialize(),allplanets))
    return jsonify(allplanets), 200

@app.route("/favorites", methods=["GET","POST", "DELETE"])
def add_delete_favorites():

    allfavorites = Favorites.query.all()
    allfavorites = list(map(lambda x: x.serialize(),allfavorites))

    return jsonify(allfavorites), 200

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=PORT, debug=False)