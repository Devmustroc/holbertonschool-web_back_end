#!/usr/bin/env python3
""" Module of Session Auth views"""

from api.v1.auth.auth import Auth
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import uuid


class SessionAuth(Auth):
    """ Session Auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return a User ID based on a Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Return a User instance based on a cookie value"""
        data = request.get_json()
        if not data:
            return jsonify({"error": "Wrong format"}), 400
        email = data.get("email", "").strip()
        password = data.get("password", "").strip()
        first_name = data.get("first_name", "").strip()
        last_name = data.get("last_name", "").strip()
        if not email:
            return jsonify({'error': 'Email is required'}), 400
        if not password:
            return jsonify({'error': 'Password is required'}), 400
        try:
            user = User()
            user.email = email
            user.password = password
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return jsonify(user.to_json()), 201
        except Exception as e:
            return jsonify({'error': f"Can't create User: {e}"}), 400

