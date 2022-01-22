#!/usr/bin/env python3
"""
This module provides extended Python class.

Module: deepnox.core.base

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

from deepnox import loggers

LOGGER = loggers.factory(__name__)
""" The main LOGGER. """


class DeepnoxDict(dict):
    def __init__(self, **kwargs):
        dict.__init__(**kwargs)
        self._attributes = {}

    def __setitem__(self, key, item):
        super().__setitem__(key, item)

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __repr__(self):
        return super().__repr__()

    def __len__(self):
        return len(super())

    def __delitem__(self, key):
        super().__delitem__(key)

    def clear(self):
        return super().clear()

    def copy(self):
        return super().copy()

    def has_key(self, k):
        return k in self

    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)

    def keys(self):
        return super().keys()

    def values(self):
        return super().values()

    def items(self):
        return super().items()

    def pop(self, *args):
        return super().pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self, dict_)

    def __contains__(self, item):
        return item in self

    def __iter__(self):
        return super().__iter__()
