#!/usr/bin/env python3

"""
Module: deepnox.clients.http_client

This file is a part of (deepnox.clients) project.

(c) 2021, Deepnox SAS.
"""

import asyncio
import logging
import sys
import time
import urllib
from types import FunctionType, TracebackType
from typing import Optional, Type
from urllib.parse import urlencode

from deepnox import loggers
from deepnox.auth.credentials import BaseAuthorization, AuthorizationType
from deepnox.network.http import HttpRequest, HttpResponse, HttpHit, HttpMethod, HttpRequestPayload
from deepnox.third import aiohttp

LOGGER = loggers.factory(__name__)
""" The module LOGGER. """

import aiohttp


def request_tracer(results_collector):
    """
    Provides request tracing to aiohttp client sessions.
    :param results_collector: a dict to which the tracing results will be added.
    :return: an aiohttp.TraceConfig object.

    :example:

    # >>> import asyncio
    # >>> import aiohttp
    # >>> from . import request_tracer
    >>>
    >>>
    >>> async def func():
    >>>     trace = {}
    >>>     async with aiohttp.ClientSession(trace_configs=[request_tracer(trace)]) as client:
    >>>         async with client.get('https://github.com') as response:
    >>>             print(trace)
    >>>
    >>> asyncio.get_event_loop().run_until_complete(func())
    {'dns_lookup_and_dial': 43.3, 'connect': 334.29, 'transfer': 148.48, 'total': 526.08, 'is_redirect': False}
    """

    async def on_request_start(session, context, params):
        context.on_request_start = session.loop.time()
        context.is_redirect = False

    async def on_connection_create_start(session, context, params):
        since_start = session.loop.time() - context.on_request_start
        context.on_connection_create_start = since_start

    async def on_request_redirect(session, context, params):
        since_start = session.loop.time() - context.on_request_start
        context.on_request_redirect = since_start
        context.is_redirect = True

    async def on_dns_resolvehost_start(session, context, params):
        since_start = session.loop.time() - context.on_request_start
        context.on_dns_resolvehost_start = since_start

    async def on_dns_resolvehost_end(session, context, params):
        since_start = session.loop.time() - context.on_request_start
        context.on_dns_resolvehost_end = since_start

    async def on_connection_create_end(session, context, params):
        since_start = session.loop.time() - context.on_request_start
        context.on_connection_create_end = since_start

    async def on_request_chunk_sent(session, context, params):
        since_start = session.loop.time() - context.on_request_start
        context.on_request_chunk_sent = since_start

    async def on_request_end(session, context, params):
        total = session.loop.time() - context.on_request_start
        context.on_request_end = total

        dns_lookup_and_dial = context.on_dns_resolvehost_end - context.on_dns_resolvehost_start
        connect = context.on_connection_create_end - dns_lookup_and_dial
        transfer = total - context.on_connection_create_end
        is_redirect = context.is_redirect

        results_collector['dns_lookup_and_dial'] = round(dns_lookup_and_dial * 1000, 2)
        results_collector['connect'] = round(connect * 1000, 2)
        results_collector['transfer'] = round(transfer * 1000, 2)
        results_collector['total'] = round(total * 1000, 2)
        results_collector['is_redirect'] = is_redirect

    trace_config = aiohttp.TraceConfig()

    trace_config.on_request_start.append(on_request_start)
    trace_config.on_request_redirect.append(on_request_redirect)
    trace_config.on_dns_resolvehost_start.append(on_dns_resolvehost_start)
    trace_config.on_dns_resolvehost_end.append(on_dns_resolvehost_end)
    trace_config.on_connection_create_start.append(on_connection_create_start)
    trace_config.on_connection_create_end.append(on_connection_create_end)
    trace_config.on_request_end.append(on_request_end)
    trace_config.on_request_chunk_sent.append(on_request_chunk_sent)

    return trace_config


_tracer = {}

class HttpClient(object):
    """
    The HTTP client.

    """

    LOG = LOGGER.getChild("HttpClient")
    """ The LOGGER. """

    def __init__(self,
                 loop: asyncio.AbstractEventLoop = None,
                 auditor_logger=None,
                 timeout: int = 30,
                 verify_ssl: bool = False,
                 auth=None,
                 raise_for_status: bool = False,
                 ):
        self.loop = loop or asyncio.get_event_loop()
        self.raise_for_status = raise_for_status
        self._cookie_jar = aiohttp.CookieJar(loop=self.loop, unsafe=True, quote_cookie=False)
        self._client = self._create_client()
        self.AUDITOR = auditor_logger or loggers.auditor(f'auditor')


    # def _store_cookies(self, domain: str):
    #     cookies = self.cookie_jar.filter_cookies(domain)
    #     print("101// Cookies", cookies)
    #     return {cookie.key: cookie.value for key, cookie in cookies.items()}

    def _create_client(self, authorization: BaseAuthorization = None, cookies: dict = None):
        _args = {"loop": self.loop,
                 "raise_for_status": self.raise_for_status,
                 "cookies": cookies,
                 }



        if isinstance(authorization, BaseAuthorization):
            _args["auth"] = authorization.instance

        return aiohttp.ClientSession(**_args)

    async def close(self) -> None:
        return await self._client.close()

    async def __aenter__(self) -> "HttpClient":
        return self

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
    ) -> Optional[bool]:
        await self.close()
        return None

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
                                elapsed_time=(end_at - req.start_at) * 1000)
        return response

    def _build_request_args(self, req: HttpRequest):
        data = {"url": str(req.url), }

        if isinstance(req.authorization, dict):
            if req.authorization.type == AuthorizationType.BEARER_TOKEN:
                headers = data.get("headers", {})
                headers.update("Autorization", f"Bearer {req.authorization.instance}")

                # print("7// bearer ", headers)

        if isinstance(req.headers, dict):
            data.update({"headers": req.headers})

        if isinstance(req.payload, HttpRequestPayload):
            if isinstance(req.payload.params, dict):
                data.update({"params": req.payload.params})
            if isinstance(req.payload.data, str):
                data.update({"data": urlencode(req.payload.data)})
            if isinstance(req.payload.data, dict):
                data.update({"data": urlencode(req.payload.data)})

        return data

    def request(self, req: HttpRequest):
        """
        Send a HTTP request.
        :param req: The request.
        :type req: :class:`deepnox.network.http.HttpRequest`
        :return:
        """
        LOGGER.debug(f'get(req:{req})', extra={"request": req.dict()})
        method = str(getattr(req, "method"))
        req.start_at = time.time()
        self._client = self._create_client(authorization=req.authorization, cookies=req.cookies)
        d = self._build_request_args(req)
        return getattr(self._client, method)(**d)

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

    def _trace_audit(self, req: HttpRequest, res: HttpResponse):
        """
        Add trace.

        :param req: The HTTP request.
        :type req: :class:`deepnox.network.http.HttpRequest`
        :param res: The HTTP response.
        :type res: :class:`deepnox.network.http.HttpResponse`
        :return:
        """
        self.LOG.debug("_trace_audit(req, res)", extra={"req": req.dict(), "res": res.dict()})
        http_hit = HttpHit(start_at=req.start_at, end_at=res.end_at,
                           url=req.url, method=req.method,
                           request=req, response=res)
        if 200 < res.status_code >= 400:
            self.LOG.error(f"Failed: ({str(req.method)} at url:{req.url})", extra=http_hit.dict())
            print(http_hit.json())
        else:
            self.LOG.info(f"Success: ({str(req.method)} at url:{req.url})", extra=http_hit.dict())

    # def __del__(self):
    #     try:
    #         asyncio.create_task(self._close_session())
    #     except RuntimeError:
    #         self.loop.run_until_complete(self._close_session())
    #
    # async def _close_session(self):
    #     if not self._session.closed:
    #         self._session.close()
