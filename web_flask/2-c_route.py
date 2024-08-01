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


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display C with its variable value"""
    my_text = text.replace('_', ' ')
    return "C {}".format(my_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
