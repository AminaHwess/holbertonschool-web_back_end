#!/usr/bin/env python3
"""Basic Babel setup"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__, template_folder="templates")
babel = Babel(app)


class Config:
    """config class for babel configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel.init_app(app, locale_selector=get_locale)


@babel.localeselector
def get_locale():
    """get_locale method that determine the best match
    with our supported languages for the client's browser"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """index method to render default template"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
