#!/usr/bin/env python3
""" Model of BasicAuth"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ Class of BasicAuth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract the Base64 part of the Basic Authorization header"""
        if authorization_header is None or not \
                isinstance(authorization_header, str):
            return None
        if not \
                authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode the Base64 Authorization header value"""
        if base64_authorization_header is \
                None or not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = \
                base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except base64.binascii.Error:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extract user email and password from
        the decoded Base64 authorization header value
        """
        if decoded_base64_authorization_header \
                is None or not \
                isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in \
                decoded_base64_authorization_header:
            return None, None
        email, password = \
            decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on
        his email and password
        """
        if user_email is None \
                or not isinstance(user_email, str):
            return None

        if user_pwd is None \
                or not isinstance(user_pwd, str):
            return None

        user_list = []
        try:
            user_list = User.search({"email": user_email})
            if user_list == []:
                return None
        except Exception:
            return None

        user = user_list[0]
        if user.is_valid_password(user_pwd):
            return user

        return None
