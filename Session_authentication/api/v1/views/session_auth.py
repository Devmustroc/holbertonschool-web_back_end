#!/usr/bin/env python3
""" View for Session Authentication """
from api.v1.views import app_views
from api.v1.app import auth
from flask import abort, jsonify, request
from api.v1.auth.session_auth import SessionAuth
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login """
    email = request.form.get("email", "")
    password = request.form.get("password", "")

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = SessionAuth().create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(os.getenv("SESSION_NAME"), session_id)

    return response


@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ DELETE /api/v1/auth_session/logout """
    if not SessionAuth().destroy_session(request):
        abort(404)

    return jsonify({}), 200
