#!/usr/bin/env python3
""" View for Session Authentication """
from flask import jsonify, abort, request
from api.v1.views import app_views
from api.v1.auth import auth
from models.user import User


@app_views.route('/auth_session/login',
                 methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login """
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

    try:
        if not request:
            return jsonify({"error": "bad request"}), 400

        session_id = auth.session_cookie(request)
        if not session_id:
            return jsonify({"error": "session ID not found"}), 400

        user_id = auth.user_id_for_session_id(session_id)
        if not user_id:
            return jsonify({"error": "user ID not found for session ID"}), 400

        destroyed = auth.destroy_session(request)
        if not destroyed:
            return jsonify({"error": "session could not be destroyed"}), 500

        return jsonify({}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
