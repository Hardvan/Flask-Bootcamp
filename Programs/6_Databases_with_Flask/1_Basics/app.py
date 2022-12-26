
# ? 1) import os module and flask_sqlalchemy
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# ? 2) get the path of the current file
base_dir = os.path.abspath(os.path.dirname(__file__))
# __file__ ---> app.py
print(base_dir)

app = Flask(__name__)

# ? 3) Connecting to the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(base_dir, "data.sqlite")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ? 4) Creating a model
class Puppy(db.Model):

    # Manual table name
    __tablename__ = "puppies"

    # Attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Used to represent the object
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old."
