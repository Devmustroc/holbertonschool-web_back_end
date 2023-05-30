#!/usr/bin/env python3
import logging
import re
import typing
import os
import mysql
import mysql.connector
from logging import StreamHandler
from typing import List, Tuple

PII_FIELDS: Tuple[str, str, str, str, str] =\
    ("name", "email", "phone_number", "address", "credit_card")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter
        class RedactingFormatter that inherits from logging.Formatter
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]) -> None:
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming log
        records using filter_datum
        """
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            message, self.SEPARATOR)


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns the log message obfuscated """
    for field in fields:
        message = re.sub(rf"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """ Returns a logging.Logger object """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to the database"""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    # Create a connection to the database
    db = mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=db_name
    )
    return db
