#!/usr/bin/env python3

from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config[
    "SECRET_KEY"
] = "bb13dc2a57ee290e328f60c4bfa12ef6"  # Will want to make this an environment variable at some point

posts = [
    {
        "author": "Steven Au",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "July 13, 2020",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "July 14, 2020",
    },
]

# Decorator - returns a function for that specific route
# Forward slash is the home page for the webpage
# Route defines where the page will go
@app.route("/")
@app.route("/home")
def home():
    return render_template(
        "home.html", posts=posts
    )  # set posts variable = to posts data (list format)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
