#!/usr/bin/env python3
""" Model of auth"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class of auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        for excluded_path in excluded_paths:
            if path.startswith(excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user """
        return None
