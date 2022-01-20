#!/usr/bin/env python3

"""
Module: deepnox.clients.http_client

This file is a part of (deepnox.clients) project.

(c) 2021, Deepnox SAS.
"""

import asyncio
import logging
import time
from types import FunctionType

from deepnox import loggers
from deepnox.network.http import HttpRequest, HttpResponse, HttpHit, HttpMethod
from deepnox.serializers.json_serializer import JsonSerializer
from deepnox.third import aiohttp

LOGGER = loggers.factory(__name__)
""" The module LOGGER. """


class HttpClient(object):
    """
    The HTTP client.

    """

    LOG = LOGGER.getChild("HttpClient")
    """ The LOGGER. """

    def __init__(self,
                 loop: asyncio.AbstractEventLoop = None,
                 auditor_logger=None,
                 ):
        self.loop = loop or asyncio.get_event_loop()
        self.AUDITOR = auditor_logger or loggers.auditor(f'auditor')

    def session(self) -> aiohttp.ClientSession:
        """
        Get the current :class:`aiohttp.ClientSession`.

        :return: The current session.
        :rtype: :class:`aiohttp.ClientSession`
        """
        return aiohttp.ClientSession(loop=self.loop)

    async def _parse_response(self, req: HttpRequest, resp: HttpResponse):
        """
        Wait the HTTP response.

        :param req: The HTTP request.
        :param resp: The HTTP response.
        :return:
        """
        logging.info(f"resp {resp}")

        text = await resp.text()
        status_code = resp.status
        end_at = time.time()
        response = HttpResponse(status_code=status_code,
                                headers=resp.headers,
                                text=text,
                                end_at=end_at,
                                elapsed_time=end_at - req.start_at)
        return response

    async def request(self, req: HttpRequest):
        """
        Send a HTTP request.
        :param req: The request.
        :type req: :class:`deepnox.network.http.HttpRequest`
        :return:
        """
        LOGGER.debug(f'get(req:{req})')
        method = str(getattr(req, "method"))
        req.start_at = time.time()
        async with self.session() as session:
            try:
                self.LOG.debug(f"req.url.to_python() {req.url}")
                session_method_fn: FunctionType = getattr(session, method)
                async with session_method_fn(str(req.url), headers=req.headers) as resp:
                    res = await self._parse_response(req, resp)
                    self._trace_audit(req, res)
            except Exception as e:
                self.LOG.error(f'Response timeout (req:{req.url}', exc_info=e)

    async def get(self, req: HttpRequest):
        """
        Send a HTTP request using the verb: GET.
        :param req: The HTTP request.
        :type req: :class:`deepnox.network.http.HttpRequest`
        """
        req.method = HttpMethod.GET
        return self.request(req)

    async def post(self, req: HttpRequest):
        """
        Send a HTTP request using the verb: POST.
        :param req: The HTTP request.
        :type req: :class:`deepnox.network.http.HttpRequest`
        """
        req.method = HttpMethod.POST
        return self.request(req)

    async def put(self, req: HttpRequest):
        """
        Send a HTTP request using the verb: PUT.
        :param req: The HTTP request.
        :type req: :class:`deepnox.network.http.HttpRequest`
        """
        req.method = HttpMethod.PUT
        return self.request(req)

    async def patch(self, req: HttpRequest):
        """
        Send a HTTP request using the verb: PATCH.
        :param req: The HTTP request.
        :type req: :class:`deepnox.network.http.HttpRequest`
        """
        req.method = HttpMethod.POST
        return self.request(req)

    async def options(self, req: HttpRequest):
        """
        Send a HTTP request using the verb: OPTIONS.
        :param req: The HTTP request.
        :type req: :class:`deepnox.network.http.HttpRequest`
        """
        req.method = HttpMethod.OPTIONS
        return self.request(req)

    async def head(self, req: HttpRequest):
        """
        Send a HTTP request using the verb: HEAD.
        :param req: The HTTP request.
        :type req: :class:`deepnox.network.http.HttpRequest`
        """
        req.method = HttpMethod.HEAD
        return self.request(req)

    def _trace_audit(self, req, res):
        http_hit = HttpHit(start_at=req.start_at, end_at=res.end_at,
                           url=req.url, method=req.method,
                           req=req.dict(), res=res.dict())
        self.AUDITOR.error(f"{'Failed' if 200 < res.status_code >= 400 else 'Success'} while " +
                           f"sending ({str(req.method)} at url:{req.url})", extra=JsonSerializer().dump(http_hit.dict()))
