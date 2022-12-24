from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    nums = [1, 2, 3, 4, 5]
    names = ["Bob", "Charlie", "Dorothy"]

    # ? Good practice to use the same name as the variable in the template
    return render_template("control.html", nums=nums, names=names)


if __name__ == "__main__":
    app.run(debug=True)
