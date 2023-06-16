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
def get_locale():
    if 'locale' in request.args and request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])



@app.before_request
def before_request():
    """Find user if any and set as global on `flask.g`"""
    user = get_user()
    if user:
        g.user = user


def get_user(user_id):
    """Get user"""
    try:
        user_id = int(request.args.get('login_as'))
        if user_id in users.keys():
            return users[user_id]
    except Exception:
        return None


@app.route('/')
def index():
    """Index"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
