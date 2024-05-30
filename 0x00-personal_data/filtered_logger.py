#!/usr/bin/env python3
"""
a function called filter_datum
that returns the log message obfuscated:
"""
import re


def filter_datum(fields, redaction, message, separator):
    """ Filter Datum """
    pattern = r'({}=[^{}]*)'.format('|'.join(fields), separator)
    return re.sub(pattern, lambda m: f"{m.group(1).split('=')[0]}={redaction}", message)
