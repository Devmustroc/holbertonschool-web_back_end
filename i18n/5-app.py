#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config app class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Get locale"""
    if 'locale' in request.args and request.args['locale'] \
            in app.config['LANGUAGES']:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """Before request"""
    user_id = request.args.get('login_as')
    if user_id:
        user = get_user(int(user_id))
        if user:
            g.user = user


def get_user(user_id):
    """Get user"""
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app.route('/')
def index():
    """Index"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
