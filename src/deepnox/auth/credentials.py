#!/usr/bin/env python3

"""
Module: "deepnox.auth.credentials

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
import aiohttp
from pydantic import validator

from deepnox.core.enumerations import DeepnoxEnum


class Credentials(object):
    pass


# !/usr/bin/env python3

"""
Module: deepnox.auth.base

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
from enum import unique
from typing import Any, Optional, Dict

from deepnox.third import pydantic

from deepnox.core.enumerations import DeepnoxEnum
from deepnox.third import aiohttp


@unique
class AuthorizationType(DeepnoxEnum):
    """
    The list of authorization types.
    """

    BASIC_AUTH: str = "basic_auth"
    """ The basic authorization type. """

    BEARER_TOKEN: str = "bearer_token"
    """ An authentication using bearer token mechanism. """

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return str(self) == str(other)


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
        if self.type == AuthorizationType.BASIC_AUTH:
            d = {"login": self.values.get("username"),
                 "password": self.values.get("password"),
                 "encoding": self.values.get("encoding", "latin1")
                 }
            return aiohttp.BasicAuth(**d)

        elif self.type == AuthorizationType.BEARER_TOKEN:
            # print("je passe ici", self.values.get("bearer_token"))
            return self.values.get("bearer_token")

    def dict(
            self,
            **kwargs
    ) -> Dict[str, Any]:
        kwargs.update({"exclude_none": True})
        return super().dict(**kwargs)
