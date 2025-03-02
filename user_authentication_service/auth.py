#!/usr/bin/env python3
"""Hash password"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """_hash_password function that that takes in
    a password string arguments and returns bytes"""
    pw_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw_bytes, salt)


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """__init__ method"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register_user method that register a new user"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email, password)
            return user
