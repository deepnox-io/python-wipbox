#!/usr/bin/env python3

"""
Utilities for exceptions management.

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""

def raise_if_param_is_none(**kwargs):
    """
    Raise a {TypeError} if provided parameter is None.

    :param name: The parameter name.
    :param value: The value of parameter.
    :return: False if parameter value is not None
    :raise: {TypeError} if value of param is None.
    """
    def _raise_exception(k):
        raise TypeError(f"Parameter is missing: type({k}) is None")

    for k, v in kwargs.items():
        if v is None:
            _raise_exception(k)

    return False


