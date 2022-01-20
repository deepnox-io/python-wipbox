#!/usr/bin/env python3

"""
Helpers to develop metaclass.
"""
from types import FunctionType

def get_attributes_by_type(attrs, type_):
    """
    Returns tye filtered list of user defined attributes from a attributes dictionary passed to the __new__ coro of a metaclass.

    :param attrs: Attributes of a metaclass (last parameters of __new__ coro).
    :return:
    :rtype: dict
    """
    return {k: v for k, v in attrs.items() if isinstance(v, type_) or issubclass(v.__class__, type_)}

def get_user_defined_functions(attrs):
    """
    Returns list of user defined functions from a attributes dictionary passed to the __new__ coro of a metaclass.

    :param attrs: Attributes of a metaclass (last parameters of __new__ coro).
    :rtype: dict
    :return:
    """
    # return get_attributes_by_type(attrs, FunctionType)
    r = {}
    for k, v in attrs.items():
        if isinstance(v, FunctionType):
            if not v.__name__.startswith('__') and not v.__name__.endswith('__'):
                r[k] = v
    return r
