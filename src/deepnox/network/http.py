#!/usr/bin/env python3

"""
Module: deepnox.tests.network.http

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
import json
from dataclasses import Field
from datetime import datetime
from enum import EnumMeta, unique
from typing import Dict, Optional, Any, Union
from uuid import UUID, uuid4

from pydantic import validator

from deepnox.core.enumerations import DeepnoxEnum
from deepnox.models import ExtendedBaseModel
from deepnox.network.urls import Url
from deepnox.serializers.json_serializer import is_json
from deepnox.third import arrow, pydantic, yaml


class HttpMethodMetaClass(EnumMeta):
    def __call__(cls, value, *args, **kwargs):
        if isinstance(value, str):
            value = value.lower()
            return super().__call__(value, *args, **kwargs)


@unique
class HttpMethod(DeepnoxEnum, metaclass=HttpMethodMetaClass):
    """
    Enumeration of HTTP methods.
    """

    GET = 'get'
    """ The HTTP GET coro. """

    POST = 'post'
    """ The HTTP POST coro. """

    PUT = 'put'
    """ The HTTP PUT coro. """

    DELETE = 'delete'
    """ The HTTP DELETE coro. """

    OPTIONS = 'options'
    """ The HTTP OPTIONS coro. """

    PATCH = 'patch'
    """ The HTTP PATCH coro. """

    HEAD = 'head'
    """ The HTTP HEAD coro. """

    @classmethod
    def get(cls, s):
        return getattr(cls, s.upper())


class HttpRequestPayload(ExtendedBaseModel, extra=pydantic.Extra.forbid, orm_mode=True):
    """
    Payload of a HTTP request.

    """

    params: Optional[Dict] = None
    """ The querystring parameters. """

    data: Optional[Union[str, Dict]] = None
    """ The raw body passed to request. """


class HttpRequest(ExtendedBaseModel, extra=pydantic.Extra.forbid, orm_mode=True):
    """
    An HTTP request.

    """

    method: HttpMethod = HttpMethod.GET
    """ The HTTP method to use. """

    url: Optional[Union[Url, Dict]] = None
    """ The targeted url."""

    headers: Optional[Dict] = None
    """ The HTTP request headers."""

    payload: Optional[HttpRequestPayload] = None
    """ The HTTP payload. """

    params: Optional[Dict] = None
    """ The parameters to send. """

    data: Optional[str] = None
    """ The data to send. """

    json_data: Optional[Dict] = None
    """ The JSON to send. """

    authorization: Optional[str] = None
    """
    The provided authorization.
    
    :todo: Implements authorization.
    """

    start_at: Optional[datetime] = None
    """ Datetime starting request. """

    end_at: Optional[datetime] = None
    """ Datetime ending request. """

    body: Optional[str]

    @validator('url', pre=True, always=True)
    def url_autoconvert(cls, v):
        if isinstance(v, Url):
            return v
        if isinstance(v, dict):
            return Url(**v)
        raise TypeError

    @validator('payload', pre=True, always=True)
    def payload_autoconvert(cls, v):
        if isinstance(v, HttpRequestPayload):
            return v
        if isinstance(v, dict):
            return HttpRequestPayload(**v)

    @property
    def size(self) -> int:
        if self.body is not None:
            return len(self.body)
        return 0

    def dict(
            self,
            **kwargs
    ) -> Dict[str, Any]:
        kwargs.update({"exclude_none": True})
        return super().dict(**kwargs)


class HttpGetRequest(HttpRequest):
    """
    The GET method for HTTP protocol.
    """

    method: HttpMethod = HttpMethod.GET
    """ The HTTP method to use. """


class HttpPostRequest(HttpRequest):
    """
    The POST method for HTTP protocol.
    """

    method: HttpMethod = HttpMethod.POST
    """ The HTTP method to use. """


class HttpPutRequest(HttpRequest):
    """
    The PUT method for HTTP protocol.
    """

    method: HttpMethod = HttpMethod.PUT
    """ The HTTP method to use. """


class HttpPatchRequest(HttpRequest):
    """
    The PATCH method for HTTP protocol.
    """

    method: HttpMethod = HttpMethod.PATCH
    """ The HTTP method to use. """


class HttpDeleteRequest(HttpRequest):
    """
    The DELETE method for HTTP protocol.
    """

    method: HttpMethod = HttpMethod.DELETE
    """ The HTTP method to use. """


class HttpOptionsRequest(HttpRequest):
    """
    The OPTIONS method for HTTP protocol.
    """

    method: HttpMethod = HttpMethod.OPTIONS
    """ The HTTP method to use. """


class HttpResponse(ExtendedBaseModel, extra=pydantic.Extra.forbid, orm_mode=True):
    """
    A response summary for HTTP protocol.
    """

    status_code: Optional[int]
    """ The HTTP status code. """

    size: Optional[int]
    """ The HTTP response size (in bytes). """

    headers: Optional[Dict]
    """ The HTTP headers as a key/value dictionary. """

    text: Optional[str]
    """ The text of the response. """

    _text_copy: Optional[str]
    """ A backup of the response text. """

    end_at: Optional[datetime]
    """ The response has been finished at... """

    elapsed_time: Optional[float]
    """ Elapsed time between receiving response and starting request. """


class HttpHit(ExtendedBaseModel):
    """
    A HTTP hit.
    """

    # request_id: UUID = Field(default_factory=uuid4)
    """ The unique request identifier. """

    status_code: Optional[int]
    """ The HTTP status code. """

    url: Optional[Url]
    """ The targeted URL. """

    method: Optional[HttpMethod]
    """ The HTTP request method. """

    start_at: Optional[datetime]
    """ Start datetime of request process. """

    end_at: Optional[datetime]
    """ End datetime of request process. """

    request: Optional[HttpRequest]
    """ The HTTP request. """

    response: Optional[HttpResponse]
    """ The HTTP response. """

    error: Optional[str]
    """ Error description if occurs. """

    @property
    def elapsed_time(self):
        if self.end_at is not None and self.start_at is not None:
            return (arrow.get(self.end_at).timestamp() - arrow.get(self.end_at).timestamp()) * 1000
        return

    class Config:
        json_encoders = {
            datetime: lambda dt: arrow.get(dt).isoformat(),
            HttpRequest: lambda req: req.dict(),
            HttpResponse: lambda res: res.dict(),
        }


def build_http_request_from_yaml_template(templates_manager=None, template_filename: str = None, ctx=None):
    """
    Build a request from a YAML template.

    :param templates_manager:
    :type:
    :return:
    """
    data = templates_manager.render(template_filename, ctx)
    d = yaml.safe_load(data)
    return HttpRequest(**d)
