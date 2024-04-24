from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"


@app.route("/dog/<name>")
def dog(name):
    # IndexError: string index out of range
    return f"<h1>{name[1000]}'s Page</h1>"


if __name__ == "__main__":
    app.run(debug=True)  # ? debug=True will show the error in the browser

    # ? Don't use debug=True in production because it will show the error in the browser
