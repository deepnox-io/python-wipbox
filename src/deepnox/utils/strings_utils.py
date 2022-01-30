#!/usr/bin/env python3

"""
String utilities.

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
import re


def remove_slash_at_start_and_at_end(s: str) -> str:
    """
    Remove slash if it's the first or last char.
    Used to normalize URL.

    :param s: String to process.
    :type s: str
    :return: A normalized string without slash
    :rtype: str
    """
    if s is None:
        return None
    r = str(s)
    if len(r) == 0:
        return r
    r = r.strip()
    if r[0] == "/":
        r = r[1:]
    if len(r) > 0 and r[len(r)-1] == "/":
        r = r[:len(r)-1]
    return r


def extract_idp_code(s) -> str:
    """
    Extract an UUID v4 from string.

    :param s: String to process.
    :type s: str
    :return: The extracted UUID.
    :rtype: str
    """
    if not s:
        return
    m = re.findall(r'([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})', s)
    if len(m) > 0:
        return m[0]
