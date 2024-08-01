#!/usr/bin/python3
"""
The art of flask web application
"""


from flask import Flask

app = Flask(__name__)
app.url_map.


@app.route('/', strict_slashes=False)
def welcome():
    """return Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display “HBNB”"""
    return 'HBNB'


@app.route('/C/<text>', strict_slashes=False)
def display_c_param(text):
    """display c parameters"""
    replace_underscore = text.replace('_', ' ')
    return "C {}".format(replace_underscore)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
