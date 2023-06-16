#!/usr/bin/env python3
"""module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Get locale"""
    languages = app.config['LANGUAGES']
    locale = request.args.get("locale")
    if locale and locale in languages:
        return locale
    return request.accept_languages.best_match(languages)


def get_user(user_id) -> Dict:
    """Returns a user"""
    login_as = request.args.get('login_as')
    if login_as and int(login_as) == user_id:
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """Finds a user if any"""
    user_id = 2  # Change the user ID according to your needs
    user = get_user(user_id)
    g.user = user


@app.route("/")
def hello_world():
    """Index"""
    try:
        username = g.user["name"]
    except Exception:
        username = None
    return render_template("5-index.html", username=username)


if __name__ == "__main__":
    app.run()
