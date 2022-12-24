from flask import Flask

app = Flask(__name__)


@app.route('/')  # 127.0.0.1:5000/
def index():
    return "<h1>Hello, World!</h1>"


@app.route("/info")  # 127.0.0.1:5000/info
def info():
    return "<h2>This is the info page</h2>"


if __name__ == "__main__":
    app.run()
