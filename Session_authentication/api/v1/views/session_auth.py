#!/usr/bin/env python3
""" View for Session Authentication """
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
@app_views.route('/auth_session/login/', methods=['POST'], strict_slashes=False)
def session_login():
    """ POST /api/v1/auth_session/login """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or email == "":
        return jsonify({"error": "email missing"}), 400
    if not password or password == "":
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 401
    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user[0].id)
    user_json = user[0].to_json()
    response = jsonify(user_json)
    response.set_cookie(getenv('SESSION_NAME'), session_id)

    return response, 200
