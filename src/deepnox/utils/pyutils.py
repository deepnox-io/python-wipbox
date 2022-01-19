#!/usr/bin/env python3

import functools
import types


def get_attributes(obj):
    return {attr_name: getattr(obj, attr_name) for attr_name in dir(obj)
                      if callable(getattr(obj, attr_name))}

def copy_func(f):
    """
    Copy a function.

    Based on:

    - http://stackoverflow.com/a/6528148/190597 (Glenn Maynard)
    - [How to create a copy of a python function](https://stackoverflow.com/a/13503277)
    """
    g = types.FunctionType(f.__code__, f.__globals__, name=f.__name__,
                           argdefs=f.__defaults__,
                           closure=f.__closure__)
    g = functools.update_wrapper(g, f)
    g.__kwdefaults__ = f.__kwdefaults__
    return g