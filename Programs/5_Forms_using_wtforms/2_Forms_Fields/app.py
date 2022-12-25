from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField, SelectField,
                     TextAreaField, SubmitField)

# ? Used for validation of form fields
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "verysecretkey"


class InfoForm(FlaskForm):

    breed = StringField("What breed is your dog?", validators=[DataRequired()])
    neutered = BooleanField("Have you neutered your dog?")
    mood = RadioField("Please choose your dog's mood:",
                      choices=[("mood_one", "Happy"),
                               ("mood_two", "Excited")])
    # .items() can be used on a dictionary to convert to this nested tuple
    food_choice = SelectField("Pick your dog's favorite food:",
                              choices=[("chi", "Chicken"),
                                       ("bf", "Beef"),
                                       ("fish", "Fish")])

    feedback = TextAreaField()
    submit = SubmitField("Submit")


@ app.route('/', methods=["GET", "POST"])
def index():

    form = InfoForm()
    if form.validate_on_submit():

        # ? Session is a dictionary that stores data for the user across different requests

        session["breed"] = form.breed.data
        session["neutered"] = form.neutered.data
        session["mood"] = form.mood.data
        session["food_choice"] = form.food_choice.data
        session["feedback"] = form.feedback.data

        # Only happens if form is submitted and validated
        return redirect(url_for("thankyou"))

    return render_template("index.html", form=form)


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)
