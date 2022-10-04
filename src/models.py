from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean, unique=False, nullable=False)
    favorites = db.relationship('Favorites')

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'People'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    description = db.Column(db.String(650))

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }



class Planets(db.Model):
    __tablename__ = 'Planets'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    description = db.Column(db.String(250)) 

    def __repr__(self):
        return '<Planets %r>' % self.title

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            # do not serialize the password, its a security breach
        }


class Favorites(db.Model):
    __tablename__ = 'Favorites'
    id = db.Column(db.Integer, primary_key=True)
    planets_id = db.Column(db.Integer, db.ForeignKey('Planets.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('People.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user = db.relationship('User', foreign_keys=[user_id])
    planets = db.relationship('Planets')
    people = db.relationship('People')

    def __repr__(self):
        return '<Favorites %r>' % self.object_id

    def serialize(self):
        return {
            "id": self.object_id
            # do not serialize the password, its a security breach
        }