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

    def session_cookie(self, request=None):
        """Return a cookie value from a request"""
        if request is None:
            return None

        session_cookie_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_cookie_name)

    def current_user(self, request=None):
        """Return a User instance based on a cookie value"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if user_id:
            user = User.get(user_id)
            return user
        return None
