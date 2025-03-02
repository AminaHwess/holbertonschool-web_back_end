#!/usr/bin/env python3
"""Hash password"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """_hash_password function that that takes in
    a password string arguments and returns bytes"""
    pw_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw_bytes, salt)


def _generate_uuid() -> str:
    """_generate_uuid method that return a
    string representation of a new UUID."""
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """valid_login method"""
        try:
            user = self._db.find_user_by(email=email)
            pw_bytes = password.encode("utf-8")
            match = bcrypt.checkpw(pw_bytes,
                                   _hash_password(user.hashed_password))
            return match
        except NoResultFound:
            return False
