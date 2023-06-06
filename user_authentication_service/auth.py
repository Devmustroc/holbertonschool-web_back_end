#!/usr/bin/env python3
"""
Auth methods
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Returns a salted, hashed password,
    which is a byte string.
    """
    byte = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(byte, salt)
    return hashed


def _generate_uuid() -> str:
    """
    Returns a string representation of a new UUID
    """
    return str(uuid.uuid4())


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
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass
        hashed = _hash_password(password).decode()
        user = self._db.add_user(email, hashed)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Checks if password is valid
        """
        try:
            usr = self._db.find_user_by(email=email)
            password = password.encode("utf-8")
            usr_pass = usr.hashed_password.encode("utf-8")
            return bcrypt.checkpw(password, usr_pass)
        except Exception:
            return False
