#!/usr/bin/env python3
"""0. Basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route("/", methods=["GET"])
def home():
    """Render home page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
