#!/usr/bin/env python3
import aiohttp


class BaseAuthorization(object):
    """
    A base class for managing authorizations/permissions.
    """

    def __init__(self, auth_obj: object = None):
        self._auth_obj = auth_obj

    @classmethod
    def from_dict(cls, d: dict) -> object:
        """
        :return: Object as a JSON string.
        """
        if not isinstance(d, dict):
            raise TypeError(f'parameter must be of type: `dict`')
        o = cls()
        for k, v in d.items():
            if k in o.__attrs__:
                setattr(o, k, v)
        return o

class HttpBasicAuth(BaseAuthorization):
    """
    An encapsulation of basic HTTP authentication.
    """

    def __init__(self, username: str = None, password: str = None, encoding: str = 'latin1'):
        self._auth_obj = aiohttp.BasicAuth(username, password, encoding)