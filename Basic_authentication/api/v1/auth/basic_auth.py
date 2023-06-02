#!/usr/bin/env python3
""" Model of BasicAuth"""
from api.v1.auth.auth import Auth


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

