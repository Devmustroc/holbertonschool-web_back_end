#!/usr/bin/env python3
""" Auth class """
from flask import request

from typing import List, TypeVar


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth"""
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        for excluded_path in excluded_paths:
            if path.rstrip("/").startswith(excluded_path.rstrip("/")):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user"""
        return None
