#!/usr/bin/env python3

"""
Module: deepnox.auth.base

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
from enum import unique
from typing import Any, Optional

import pydantic

from deepnox.core.enumerations import DeepnoxEnum
from deepnox.third import aiohttp

@unique
class AuthorizationType(DeepnoxEnum):
    """
    The list of authorization types.
    """

    BASIC_AUTH = "basic_auth"
    """ The basic authorization type. """



class BaseAuthorization(pydantic.BaseModel):
    """
    The base class for authorization.
    """

    type: Optional[AuthorizationType] = None
    """ The authorization type. """

    @property
    def instance(self) -> int:
        raise NotImplementedError



class BasicAuthorization(BaseAuthorization):
    """
    The basic authorization.
    """

    type: AuthorizationType = AuthorizationType.BASIC_AUTH
    """ The basic authorization type. """

    username: str = None
    """ The username. """

    password: str = None
    """ The password. """

    encoding: str = 'latin1'
    """ The language encoding. """

    @property
    def instance(self) -> int:
        return aiohttp.BasicAuth(login=self.username, password=self.password, encoding=self.encoding)