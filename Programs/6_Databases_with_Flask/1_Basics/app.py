
# ? 1) import os module and flask_sqlalchemy
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Used to migrate the database

# ? Type set FLASK_APP=app.py in the terminal to set the environment variable
# ? If it doesn't work, type $env:FLASK_APP="app.py" in the terminal

# ? 2) get the path of the current file
base_dir = os.path.abspath(os.path.dirname(__file__))  # __file__ ---> app.py
print(f"Base directory: {base_dir}")

app = Flask(__name__)

# ? 3) Connecting to the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(base_dir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Migrate(app, db)  # Connects the app to the database

# * Terminal Commands for Flask Migrate
# ? `flask db init`: create the migrations folder
# ? `flask db migrate -m "Initial migration"`: create the migration file
# ? `flask db upgrade`: create the database


# ? 4) Creating a model
class Puppy(db.Model):

    # Manual table name
    __tablename__ = "puppies"

    # Attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    # Constructor
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Used to represent the object
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old."
