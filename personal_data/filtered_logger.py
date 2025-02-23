#!/usr/bin/env python3
"""Encrypting passwords Check & valid password"""


import bcrypt


def hash_password(password: str) -> bytes:
    """hash_password function that  returns a salted, hashed password"""
    bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """is_valid function that the provided password
    matches the hashed password"""
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)

