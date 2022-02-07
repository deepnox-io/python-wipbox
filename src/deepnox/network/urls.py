#!/usr/bin/env python3

"""

# Module: loadguard.core.web.url

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.

This module provides utilities to manage URLs.

"""

from typing import Dict, Optional, Union, Any
from urllib.parse import ParseResult, urlencode

from deepnox import loggers
from deepnox.models import ExtendedBaseModel
from deepnox.third import pydantic
from deepnox.network import Scheme
from deepnox.utils.strings_utils import remove_slash_at_start_and_at_end

LOGGER = loggers.factory(__name__)
""" The main LOGGER. """


class Url(ExtendedBaseModel):
    """
    Url entity.

    Encapsulation of Python :class:`urllib.parse.ParseResult`.
    """

    scheme: Optional[Scheme] = None
    """ The scheme. """

    hostname: Optional[str] = None
    """ The hostname. """

    port: Optional[int] = None
    """ The port. """

    path: Optional[str] = None
    """ The path. """

    # __attrs__ = ['scheme', 'netloc', 'path', 'params', 'query', 'hostname', 'port']
    # __attrs__ = ["scheme", "hostname", "port", "path"]

    def to_python(self) -> ParseResult:
        """
        Convert instance to native `class`:urllib.parser.ParseResult: object.

        :return:
        :rtype: :class:`urllib.parser.ParseResult`
        """
        return ParseResult(self.scheme, self.netloc, self.path, self.params, self._query, None)

    @pydantic.validator('scheme', pre=True, always=True)
    def scheme_autoconvert_or_default(cls, v):
        if isinstance(v, Scheme):
            return v
        if isinstance(v, str):
            return Scheme(v)

    # @property
    # def netloc(self):
    #     if self.port:
    #         return f"{self.host}:{self.port}"
    #     return self.host

    def __str__(self):
        url = f"{str(self.scheme)}://" + "/".join(
            [remove_slash_at_start_and_at_end(self.hostname), self.path])
        # url = self._add_query_string_params_to_url(url)
        return url

    def __repr__(self):
        return f'<Url ({str(self)})>'

    # def _add_query_string_params_to_url(self, url: str):
    #     if self.params is not None and len(self.params.keys()) > 0:
    #         return f"{str(self.scheme)}://{self.hostname}/{self.path}?{urlencode(self.params)}"
    #     return url

    def dict(
            self,
            **kwargs
    ) -> Dict[str, Any]:
        kwargs.update({"exclude_none": True})
        return super().dict(**kwargs)

    class Config:
        json_encoders = {
            Scheme: lambda s: str(s),
        }
        dict_encoders = {
            Scheme: lambda s: str(s),
        }
        extra = pydantic.Extra.forbid
