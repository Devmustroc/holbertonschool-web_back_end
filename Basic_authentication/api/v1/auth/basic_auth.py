#!/usr/bin/env python3
""" Basic authentication"""
import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract_base64_authorization_header"""
        if authorization_header is None or not \
                isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        base64_part = authorization_header.replace("Basic ", "")
        return base64_part.strip()

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header"""
        if (
                base64_authorization_header is None
                or not isinstance(base64_authorization_header, str)
        ):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except base64.binascii.Error:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """extract_user_credentials"""
        if (
            decoded_base64_authorization_header is None
            or not isinstance(decoded_base64_authorization_header, str)
            or ':' not in decoded_base64_authorization_header
        ):
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """user_object_from_credentials"""
        if (
                user_email is None
                or not isinstance(user_email, str)
                or user_pwd is None
                or not isinstance(user_pwd, str)
        ):
            return None
        user_list = User.search({"email": user_email})
        if not user_list:
            return None

        user = user_list[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user
