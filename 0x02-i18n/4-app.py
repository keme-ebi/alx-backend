#!/usr/bin/env python3
"""Flask babel"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """determines the best match with the supported languages"""
    # check if locale parameter is present
    if 'locale' in request.args:
        locale = request.args['locale']
        # check if the value is supported
        if locale in app.config['LANGUAGES']:
            return locale
    # default
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """render html"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
