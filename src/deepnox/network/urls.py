#!/usr/bin/env python3

"""

# Module: loadguard.core.web.url

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.

This module provides utilities to manage URLs.

"""

from typing import Dict, Optional
from urllib.parse import ParseResult, urlencode

from deepnox import loggers
from deepnox.models import ExtendedBaseModel
from deepnox.third import pydantic
from deepnox.network import Scheme
from deepnox.utils.strings_utils import remove_slash_at_start_and_at_end

LOGGER = loggers.factory(__name__)
""" The main LOGGER. """


class Url(ExtendedBaseModel, extra=pydantic.Extra.forbid, orm_mode=True):
    """
    Url entity.

    Encapsulation of Python :class:`urllib.parse.ParseResult`.
    """
    scheme: Scheme = None
    path: Optional[str] = None
    params: Optional[Dict] = None
    host: Optional[str] = None
    port: Optional[int] = None
    _query: str = None



    __attrs__ = ['scheme', 'netloc', 'path', 'params', 'query', 'hostname', 'port']

    def to_python(self) -> ParseResult:
        """
        Convert instance to native `class`:urllib.parser.ParseResult: object.

        :return:
        :rtype: :class:`urllib.parser.ParseResult`
        """
        return ParseResult(self.scheme, self.netloc, self.path, self.params, self._query, None)

    @property
    def netloc(self):
        if self.port:
            return f"{self.host}:{self.port}"
        return self.host

    def __str__(self):
        url = f"{str(self.scheme)}://" + "/".join(
            [remove_slash_at_start_and_at_end(self.host), remove_slash_at_start_and_at_end(self.path)])
        url = self._add_query_string_params_to_url(url)
        return url

    def __repr__(self):
        return f'<Url ({str(self)})>'

    def _add_query_string_params_to_url(self, url: str):
        if self.params is not None and len(self.params.keys()) > 0:
            return f"{str(self.scheme)}://{self.host}/{self.path}?{urlencode(self.params)}"
        return url
