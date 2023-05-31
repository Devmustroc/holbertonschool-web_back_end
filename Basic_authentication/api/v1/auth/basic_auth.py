#!/usr/bin/env python3
""" Basic authentication"""
from api.v1.auth.auth import Auth
import base64


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
