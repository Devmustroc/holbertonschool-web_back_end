#!/usr/bin/env python3
"""
encrypt_password.py
"""
import bcrypt
from bcrypt import hashpw, gensalt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password, which is a byte string"""
    salt = gensalt()
    hashed = hashpw(password.encode(), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates if the provided password matches the hashed password"""
    return bcrypt.checkpw(password.encode(), hashed_password)
