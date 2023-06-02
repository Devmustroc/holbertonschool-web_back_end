#!/usr/bin/env python3
""" Module of Session Auth views"""

from api.v1.auth.auth import Auth
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os
import uuid


class SessionAuth(Auth):
    """
    Session authentication
    """
    user_id_by_session_id = {}
    session_cookie_name = os.getenv("SESSION_NAME")

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Return a User ID based on a Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Returns a User instance based on a cookie value
        """
        if request is None:
            return None
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Deletes the user session / logs out
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False

        del self.user_id_by_session_id[session_id]
        return True

    def session_cookie(self, request=None):
        """
        Returns the value of a cookie from a request
        """
        if request is None:
            return None
        return request.cookies.get(self.session_cookie_name)
