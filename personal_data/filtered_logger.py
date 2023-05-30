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
import re
import typing


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)


def filter_datum(fields: typing.List[str], redaction: str, message: str, separator: str) -> str:
    return re.sub(fr'({separator})(' + '|'.join(fields) + fr')({separator})', fr'\1{redaction}\3', message)
