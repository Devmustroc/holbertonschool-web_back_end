#!/usr/bin/env python3
"""
This module provides authentication functionality for the API.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path."""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excluded_path in excluded_paths:
            if path.rstrip("/") == excluded_path.rstrip("/"):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get the value of the Authorization header from the request."""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current authenticated user."""
        return None

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extract the Base64 part of the Authorization header."""
        if authorization_header is None or not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[1]
