from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Welcome to Puppy Latin!</h1> <br /> <h3>Go to puppy_latin/<name> to see the modified name!"


@app.route("/puppy_latin/<name>")
def puppy_latin(name):
    if name[-1] == 'y':
        return f"<h2>Original: {name}</h2> <h2>Modified: {name[:-1]}iful</h2>"
    else:
        return f"<h2>Original: {name}</h2> <h2>Modified: {name}y</h2>"


if __name__ == "__main__":
    app.run(debug=True)
