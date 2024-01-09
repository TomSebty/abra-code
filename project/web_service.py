"""
This is a basic webservice
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    A simple hello world route
    """
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
