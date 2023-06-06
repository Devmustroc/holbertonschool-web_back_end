#!/usr/bin/env python3
from flask import Flask, request, jsonify
from auth import Auth

Auth = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """ GET /
    Return:
      - welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=["POST"], strict_slashes=False)
def user() -> str:
    """End-point to register a user"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": "{}".format(email), "message": "user created"})



if __name__ == '__main__':
    app.run()
