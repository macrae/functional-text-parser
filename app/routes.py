import os
import sys
from app import app
from flask import Flask, jsonify, abort, make_response, request, url_for
# from flask_httpauth import HTTPBasicAuth

sys.path.insert(0, os.path.abspath('./functions'))

from rle import rle

# auth = HTTPBasicAuth()


# @auth.get_password
# def get_password(username):
#     if username == 'kevin':
#         return 'python'
#     return None


# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({'error': 'Unauthorized access'}))


# app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/echo', methods=['GET'])
def hello_world():
    return jsonify({'hello': 'world'})


@app.route('/encode/<string:s>', methods=['GET'])
def encode(s):
    encoded_string = rle(s)
    return jsonify({'encode': encoded_string})


if __name__ == '__main__':
    app.run(debug=True)
