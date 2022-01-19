#!/usr/bin/env python

# https://code.activestate.com/recipes/576586-dot-style-nested-lookups-over-dictionary-based-dat/
from typing import Dict, Type

from deepnox import loggers

LOGGER = loggers.factory(__name__)
""" The module LOGGER. """

class Map(dict):
    """
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """

    def __init__(self, *args, **kwargs):
        try:
            super(Map, self).__init__(*args, **kwargs)
        except ValueError as e:
            LOGGER.error("ValueError while creating class:`deepnox.utils.maps.Map`", exc_info=e)
            raise CannotConvertToMapTypeError(param=str({"_args": args, "_kwargs": kwargs}))
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v
        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        if type(value) == dict and not isinstance(value, Map):
            self.__setitem__(key, Map(value))
        else:
            super().__setitem__(key, value)
            self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]


class UpperMap(Map):

    def __setitem__(self, key, value):
        if type(value) == dict and not isinstance(value, UpperMap):
            self.__setitem__(key, UpperMap(value))
        else:
            super().__setitem__(key, value)
            self.__dict__.update({key: value})

    def __getattr__(self, attr):
        return self.get(attr.lower())


class CannotConvertToMapTypeError(Exception):
    """
    Exception: cannot convert object to :class:``deepnox.utils.maps.Map`.
    """

    def __init__(self, param, message: str = None) -> None:
        """
        Create a new class:`CannotConvertToMapTypeError` exception.
        :param param: The parameter that cannot be converted.
        :param message: An optional alternative message.
                        Default message is: "The parameter ({param}) must be of type character
                        [dict|`deepnox.utils.maps.Map`] but found: (type({param})={type({param})})."
        """
        message = message or f"The parameter ({param}) must be of type character [dict|`deepnox.utils.maps.Map`] but found: (type({param})={type({param})})."
        self.parameter_name = param
        self.message = message
        super().__init__(self.message)


def to_map(o: Type[Dict] = None):
    """
    Convert a dict or derived class to :class:`deepnox.utils.maps.Map`.

    :param o: The dictionary to convert.
    :type o: dict
    :return: The map based on dictionary. An empty :class:`deepnox.utils.maps.Map` object if parameter is None.
    :rtype: :class:`deepnox.utils.maps.Map`
    :raises :class:`deepnox.utils.maps.CannotConvertToMapTypeError`: The provided paramater is not a dictionary.
    """
    if o is None:
        return Map()
    if isinstance(o, Map):
        return o
    elif isinstance(o, dict):
        return Map(o)
    raise CannotConvertToMapTypeError(param=o)
