#!/usr/bin/env python3
""" View for Session Authentication """
from flask import jsonify, abort, request
from api.v1.views import app_views
from api.v1.auth import auth
from models.user import User


@app_views.route('/auth_session/login',
                 methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    POST /api/v1/auth_session/login
    Logs in a user by creating a new Session ID
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or email == "":
        return jsonify({"error": "email missing"}), 400

    if not password or password == "":
        return jsonify({"error": "password missing"}), 400

    try:
        user_list = User.search({"email": email})
        if not user_list:
            return jsonify({"error": "no user found for this email"}), 404
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    user = user_list[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    cookie_name = os.getenv("SESSION_NAME")
    response = jsonify(user.to_json())
    response.set_cookie(cookie_name, session_id)

    return response


@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """
    DELETE /auth_session/logout
    Deletes the user session
    """
    from api.v1.app import auth
    result = auth.destroy_session(request)
    if not result:
        abort(404)

    return jsonify({}), 200