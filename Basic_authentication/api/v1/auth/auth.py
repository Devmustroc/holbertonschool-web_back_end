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
        return False

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current authenticated user."""
        return None
