#!/usr/bin/env python3
"""Flask babel"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user() -> Union[Dict, None]:
    """returns a user dictionary or None if the ID cannot be found
        or if login_as was not passed
    """
    id_value = request.args.get('login_as', None)
    if id_value is not None and int(id_value) in users.keys():
        return users.get(int(id_value))
    return None


@app.before_request
def before_request():
    """gets executed before all other functions, it uses get_user to find
        a user if any, and set it as a global on flask.g.user
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """determines the best match with the supported languages"""
    # check if locale parameter is present
    if 'locale' in request.args:
        locale = request.args['locale']
        # check if the value is supported
        if locale in app.config['LANGUAGES']:
            return locale
    # user's prefered local
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale
    # from request header
    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale
    # default
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """render html"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
