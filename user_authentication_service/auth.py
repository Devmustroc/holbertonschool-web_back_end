#!/usr/bin/env python3
"""
Auth methods
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt


def _hash_password(password: str) -> bytes:
    """Returns a salted, hashed password, which is a byte string"""
    byte = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(byte, salt)
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers and returns a new user if email isn't listed
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError (f"User {email} already exists")
        except NoResultFound:
            pass
        hashed = _hash_password(password).decode()
        user = self._db.add_user(email, hashed)
        return user
