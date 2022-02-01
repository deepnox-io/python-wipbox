#!/usr/bin/env python3

"""
Module: deepnox.auth.base

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
from enum import unique
from typing import Any, Optional, Dict

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

    def __str__(self):
        return self.value


class BaseAuthorization(pydantic.BaseModel):
    """
    The base class for authorization.
    """

    type: Optional[AuthorizationType] = None
    """ The authorization type. """

    values: Optional[Dict] = {}
    """ """

    @property
    def instance(self) -> Any:
        #if self.type == AuthorizationType.BASIC_AUTH:
            d = {"login": self.values.get("username"),
                 "password": self.values.get("password"),
                 "encoding": self.values.get("encoding", "latin1")
                 }
            return aiohttp.BasicAuth(**d)

    def dict(
            self,
            **kwargs
    ) -> Dict[str, Any]:
        kwargs.update({"exclude_none": True})
        return super().dict(**kwargs)
