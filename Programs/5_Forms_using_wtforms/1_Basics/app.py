from flask import Flask, render_template

# ? 1) Import these two lines to use forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

# ? 2) Add a secret key to use forms
app.config["SECRET_KEY"] = "verysecretkey"


# ? 3) Create a class for the form
class InfoForm(FlaskForm):

    breed = StringField("What breed is your dog?")
    submit = SubmitField("Submit")


@app.route('/', methods=["GET", "POST"])
def index():

    breed = False  # ? Different from breed in InfoForm

    # ? 4) Create an instance of the form
    form = InfoForm()

    # ? 5) Validate the form on submit and get the data
    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = ""

    # ? 6) Pass the form and the breed to the template
    return render_template("index.html", form=form, breed=breed)


if __name__ == "__main__":
    app.run(debug=True)
