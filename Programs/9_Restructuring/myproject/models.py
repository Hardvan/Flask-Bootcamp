
# ? Setup db inside the __init__.py file under myproject folder
from myproject import db


class Puppy(db.Model):

    __tablename__ = "puppies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship("Owner", backref="puppy", uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy Name: {self.name}, Owner: {self.owner.name}"
        else:
            return f"Puppy Name: {self.name} and no owner yet!"


# ? OWNERS SECTION
class Owner(db.Model):

    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey("puppies.id"))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner Name: {self.name}"
