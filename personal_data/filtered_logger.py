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
import re


def filter_datum(fields: list, redaction: str, message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    return re.sub(fr'({separator})(' + '|'.join(fields) + fr')({separator})', fr'\1{redaction}\3', message)
