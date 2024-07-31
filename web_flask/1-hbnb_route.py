#!/usr/bin/python3
"""Flask web application
python web framework
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome():
    """A function that execute code
    for home page
    """
    return 'Hello HBNB!'


@pp.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    A function that display “HBNB”
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
