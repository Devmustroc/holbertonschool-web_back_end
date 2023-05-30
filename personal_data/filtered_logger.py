#!/usr/bin/env python3
"""function called filter_datum that returns the log message obfuscated:
Arguments:
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating all
    fields in the log line (message)
The function should use a regex to replace occurrences of certain field values
"""
import logging
import csv
import re
import typing
from logging import StreamHandler
from typing import List, Tuple

PII_FIELDS: Tuple[str, str, str, str, str] = ("name", "email", "phone_number", "address", "credit_card")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter
        class RedactingFormatter that inherits from logging.Formatter
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming log records using filter_datum """
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
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
