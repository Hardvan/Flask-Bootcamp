
# ? 1) Create a folder named templates in the same directory as the python file
# ? 2) Create a file named basic.html in the templates folder
# ? 3) Import render_template function to render html files

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("basic.html")


if __name__ == "__main__":
    app.run(debug=True)
