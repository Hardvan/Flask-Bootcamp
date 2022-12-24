
# ? 1) cd to the directory where the file is located
# ? 2) Run the file using the command: python basic.py
# Default port is localhost:5000

from flask import Flask

app = Flask(__name__)  # ? Creating application object of class Flask


# ? Creating a route for home page
@app.route('/')  # Decorator
def index():
    return "<h1>Hello, World!</h1>"


if __name__ == "__main__":
    app.run()
