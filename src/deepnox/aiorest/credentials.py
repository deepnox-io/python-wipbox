#!/usr/bin/env python3

"""
Module: deepnox.aiorest.credentials

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
import aiohttp

from deepnox.core.enumerations import DeepnoxEnum


class Credentials(object):
    pass


class BasicAuth(Credentials):
    def __init__(self, username: str, password: str, encoding: str = "latin1"):
        super().__init__()
        self._username, self._password, self._encoding = (
            username,
            password,
            encoding,
        )

    def get(self):
        return aiohttp.BasicAuth(
            self._username, self._password, self._encoding
        )


class AuthorizationType(DeepnoxEnum):
    """
    The different supported credentials type.
    """

    NO_AUTH = 0
    """ No authentication. """

    API_KEY = 1
    """ The authentication based on a bearer token. """

    BEARER_TOKEN = 2
    """ The authentication based on a bearer token. """

    BASIC_AUTH = BasicAuth
    """ The HTTP basic authentication. """

    def __instancecheck__(self, instance):
        if issubclass(self.value, instance.__class__):
            return True
        return False
