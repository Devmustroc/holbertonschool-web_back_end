#!/usr/bin/env python3
"""
Auth methods
"""
from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
import bcrypt


def _hash_password(password: str) -> bytes:
    """Returns a salted, hashed password, which is a byte string"""
    byte = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(byte, salt)
    return hashed
