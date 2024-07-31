#!/usr/bin/python3
"""Flask web application
python web framework
"""

from flask import Flask


app = Flask(__name__)


@pp.route('/hbnb/', strict_slashes=False)
def hbnb():
    """
    A function that display “HBNB”
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
