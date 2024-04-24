from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"


# ? Use <> to create a dynamic route
@app.route("/dog/<name>")
def dog(name):
    return f"<h1>{name}'s Page</h1>"


if __name__ == "__main__":
    app.run(debug=True)
