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

class Planets(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(250), nullable=False)