#!/usr/bin/env python3
"""Route module for the API"""
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
def get_locale():
    # Check if locale is provided in URL parameters
    if 'locale' in request.args and request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']

    # Check if user is logged in and has a preferred locale
    if hasattr(g, 'user') and g.user and 'locale' in g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Check if locale is provided in request header
    if request.accept_languages:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    # Return default locale
    return app.config['BABEL_DEFAULT_LOCALE']


def get_user() -> Dict:
    """Returns a user dictionary or None if the ID cannot be found"""
    try:
        user_id = int(request.args.get("login_as"))
        if user_id in users.keys():
            return users[user_id]
    except Exception:
        return None


@app.before_request
def before_request():
    user_id = request.args.get('login_as', default=None, type=int)
    user = get_user(user_id)
    g.user = user


@app.route("/")
def hello_world():
    """Route for index"""
    try:
        username = g.user["name"]
    except Exception:
        username = None
    return render_template("5-index.html", username=username)


if __name__ == "__main__":
    app.run()
