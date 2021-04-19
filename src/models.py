from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
            # esto es lo que se va a exponerme por eso no se puede enviar datos sensibles en la serialización
        }

class People(db.Model):
   #__tablename__ = 'People'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(250), nullable=False)
   birth_year = db.Column(db.String(250), nullable=False)
   gender = db.Column(db.String(250), nullable=False)
   height = db.Column(db.Integer, nullable=False)
   skin_color = db.Column(db.String(250), nullable=False)
   hair_color = db.Column(db.String(250), nullable=False)
   eye_color = db.Column(db.String(250), nullable=False)
   #like = relationship(Favorites)

   def __repr__(self):
        return '<People %r>' % self.name

   def serialize(self):
       return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "skin_color": self.skin_color,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter,
            "terrain": self.terrain,
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    People_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    fav_planets = db.relationship("Planets")
    fav_characters = db.relationship("People")
    fav_user = db.relationship("User")

    def __repr__(self):
        return '<Favorites %r>' % self.user_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets_id": self.planets_id,
            "people_id": self.People_id,
         }