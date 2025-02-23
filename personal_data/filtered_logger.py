#!/usr/bin/env python3
"""Regex-ing"""

from typing import List
import re
import logging
import os
import mysql.connector


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """__init__ method"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format method to filter values in incoming log records"""
        return filter_datum(
            self.fields, self.REDACTION, super().format(record), self.SEPARATOR
        )


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """filter_datum function"""
    for field in fields:
        message = re.sub(
            f"{field}=.*?{separator}", f"{field}={redaction}{separator}", message
        )

    return message


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """get_logger function that returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(RedactingFormatter)
    logger.addHandler(streamHandler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """get_db function that  returns a connector to the database"""
    dbUser = os.getenv("PERSONAL_DATA_DB_USERNAME")
    dbPass = os.getenv("PERSONAL_DATA_DB_PASSWORD")
    dbHost = os.getenv("PERSONAL_DATA_DB_HOST")
    dbName = os.getenv("PERSONAL_DATA_DB_NAME")
    dbConnection = mysql.connector.connect(
        user=dbUser, password=dbPass, host=dbHost, database=dbName
    )
    return dbConnection


def main():
    """main function"""
    dbConnection = get_db()
    cursor = dbConnection.cursor()
    cursor.execute("Select name, email, phone, ssn, password;")
    logger = get_logger()
    for row in cursor: 
        msg = [
            f"name={row[0]};email={row[1]};phone={row[2]};ssn={row[3]};password={row[4]};ip={row[5]};last_login={row[6]};user_agent={row[7]};"
        ]
        res = RedactingFormatter.format(msg)
        logger.info(res)


if __name__ == "__main__":
    main()
