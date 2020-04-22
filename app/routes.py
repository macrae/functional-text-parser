import os
import sys
from app import app
from app.functions import rle
from flask import Flask, jsonify, make_response


@app.route("/encode/api/v1.0/<string>", methods=["GET"])
def encode(string):
    encoded_string = rle.rle(string)
    return jsonify({"encode": encoded_string})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
