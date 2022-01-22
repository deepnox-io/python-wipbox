#!/usr/bin/env python3

"""
Datetime utilities.

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

import arrow

DTKEY_FORMAT = "YYYYMMDDHHmm"

def get_dtkey(dt):
    """
    Returns datetime key used to define period store.
    """
    return arrow.get(dt).format(DTKEY_FORMAT)

