#!/usr/bin/env python3
from flask import Flask, request, jsonify
from auth import Auth

app = Flask(__name__)

Auth = Auth()


@app.route('/', methods=['GET'])
def index():
    """ GET /
    Return:
      - welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def user_register():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = Auth.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    POST /sessions
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if Auth.valid_login(email, password):
        session_id = Auth.create_session(email)
        response = jsonify({"email": "{}".format(email), "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


if __name__ == '__main__':
    app.run(debug=True)
