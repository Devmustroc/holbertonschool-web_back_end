#!/usr/bin/env python3
"""
Session authentication views
"""

from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from os import getenv
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    POST /auth_session/login
    Returns the dictionary representation of the User
    or error status code if the user can't be found
    """
    email = request.form.get("email")
    if not email or email == "":
        return jsonify({"error": "email missing"}), 400

    password = request.form.get("password")
    if not password or password == "":
        return jsonify({"error": "password missing"}), 400

    user_list = User.search({"email": email})
    if not user_list:
        return jsonify({"error": "no user found for this email"}), 404

    user = user_list[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    cookie_name = getenv("SESSION_NAME")
    response = jsonify(user.to_json())
    response.set_cookie(cookie_name, session_id)

    return response

@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    """ view for route /auth_session/logout, method DELETE """
    from api.v1.app import auth
    destroy_session = auth.destroy_session(request)
    if destroy_session is False:
        abort(404)
    else:
        return jsonify({}), 200
