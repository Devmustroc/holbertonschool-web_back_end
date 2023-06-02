#!/usr/bin/env python3
""" Model of auth"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """ Class of auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        for excluded_path in excluded_paths:
            if path.rstrip('/').startswith(excluded_path.rstrip('/')):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user """
        return None

    def session_cookie(self, request=None):
        """Return a cookie value from a request"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
