import os
from flask_dance.contrib.google import make_google_blueprint, google
from flask import Flask, redirect, url_for, render_template

# This is only needed while using a development server (i.e. localhost)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'


app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecret"

# Create the blueprint and register it
blueprint = make_google_blueprint(
    client_id="1009251394131-ujb6eqvh2igfut9res3b7rpako6f04o7.apps.googleusercontent.com",
    client_secret="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",
    offline=True, scope=["profile", "email"])

app.register_blueprint(blueprint, url_prefix="/login")


@app.route('/')
def index():
    return render_template("home.html")


@app.route("/welcome")
def welcome():
    # Return Error if not logged in
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email = resp.json()["email"]

    return render_template("welcome.html")


@app.route("/login/google")
def login():

    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email = resp.json()["email"]

    return render_template("welcome.html", email=email)


if __name__ == "__main__":
    app.run()
