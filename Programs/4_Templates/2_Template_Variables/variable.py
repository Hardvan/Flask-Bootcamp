from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():

    name = "Hardvan"
    letters = list(name)
    puppy_dictionary = {"name": "Bobo", "age": 3, "color": "brown"}
    # ? Pass the variables to the template
    return render_template("variable.html", var=name, lst=letters, diction=puppy_dictionary)


if __name__ == "__main__":
    app.run(debug=True)
