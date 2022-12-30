from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField("Puppy Name: ")
    submit = SubmitField("Add Puppy")


class DelForm(FlaskForm):

    # ID instead of name, because name is not unique
    id = IntegerField("ID Number of Puppy to Remove: ")
    submit = SubmitField("Remove Puppy")
