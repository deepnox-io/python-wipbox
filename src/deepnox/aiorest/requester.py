import asyncio
import json
import logging
import sys
import time

import aiohttp
from aiohttp import TCPConnector

from deepnox import loggers
from deepnox.aiorest.service import Resource
from deepnox.auth.base import BaseAuthorization
from deepnox.network.http import HttpMethod
from deepnox.network.http import HttpResponse
from deepnox.network.urls import Url
from deepnox.serializers.json_serializer import is_json
from deepnox.utils.metacls import get_attributes_by_type

LOGGER = loggers.factory(__name__)
""" The main LOGGER. """


class RestClientMetaclass(type):
    """
    The metaclass to create a derived class of {AioRestClient}.
    """

    LOG = LOGGER.getChild('RestClientMetaclass')
    """ The metaclass LOGGER. """

    def __new__(mcs, clsname, bases, attrs):
        """
        The `__new__` method.

        :param clsname: The class name.
        :param bases: The base classes.
        :param attrs: The attributes of the created class.
        """
        # RestClientMetaclass.LOG.debug("__new__(mcs, clsname, bases, attrs)",
        #                               extra={"mcs": mcs, "clsname": clsname, "bases": bases, "attrs": attrs})
        new_attrs = attrs  # Copy coriginal attributes to the target containing new attributes.
        new_attrs["_services"] = {}  #

        # For each web service found in the list, store name and value of the service in a dictionary of the class
        for k, v in get_attributes_by_type(attrs, Resource).items():
            new_attrs["_services"][k] = v

        # Returns a class with new attributes and/or functions.
        return super(RestClientMetaclass, mcs).__new__(mcs, clsname, bases, new_attrs)

    def __call__(self, *args, **kwargs):
        """
        The __call__ method.

        :param args: The arguments.
        :param kwargs: The kwargs.
        :return: ? (sic)

        :todo: confirm utility ?
        """
        self.LOG.debug("__call__(self, *args, **kwargs)", extra={"_args": args, "_kwargs": kwargs})
        obj = self.__new__(self, *args, **kwargs)
        obj.__init__(*args, **kwargs)
        for k, services_obj in obj._services.items():
            self.LOG.debug(f"__call__(self, *args, **kwargs): inject {obj} in {services_obj}", extra={
                "k": k,
                "obj": obj,
                "services_obj": services_obj,
            })
            setattr(services_obj, "client", obj)
        return obj


class AioRestClient(object, metaclass=RestClientMetaclass):
    LOG = LOGGER.getChild('AioRestClient')
    """ The class LOGGER. """

    def __init__(self,
                 loop: asyncio.AbstractEventLoop = None,
                 base_url: Url = None,
                 common_headers: str = None,
                 verify_ssl: bool = False,
                 auth: BaseAuthorization = None,
                 requote_redirect_url: bool = False,
                 auditor_logger: logging.Logger = None,
                 ):
        """
        Create a new instance of {AioRestClient}.

        :param loop: The event loop.
        :type loop: asyncio.AbstractEventLoop
        :param base_url: The base URL of the group of services.
        :type base_url: Url
        :param common_headers: HTTP headers used when invoking any API endpoint.
        :param verify_ssl: Boolean to set if TLS/SSL certificates must be verified.
        :type verify_ssl: bool
        """
        self.loop: asyncio.AbstractEventLoop = loop or asyncio.get_event_loop()
        self.base_url: Url = base_url
        self._common_headers = common_headers
        self.history = []
        self._connector = self._create_connector(verify_ssl=verify_ssl)
        self._auth = auth
        self._session = None
        self._requote_redirect_url = requote_redirect_url
        self.AUDITOR = auditor_logger or self.LOG


    def _create_connector(self, **kwargs) -> TCPConnector:
        """
        Return a connector without TLS verification by default.

        :param kwargs: The arguments to pass when creating the TCP connector.
        :return:
        """
        kwargs["verify_ssl"] = kwargs.get("verify_ssl") or False
        # kwargs["raise_for_status"] = kwargs.get("raise_for_status") or True
        if kwargs.get("authentication"):
            kwargs["auth"]

        return aiohttp.TCPConnector(**kwargs)

    async def _fetch(self, **kwargs):
        """
        Send an asynchronous HTTP request.

        :return:
        """
        url = kwargs.get("url")
        method = kwargs.get('method') or HttpMethod.GET
        basic_auth = kwargs.get('basic_auth')
        for item in ["method", "url", "basic_auth"]:
            if item in kwargs.keys():
                del kwargs[item]

        self.LOG.debug(f"_request(self, **kwargs)", extra={"url": url, "method": method})

        start_ts = time.monotonic()
        http_response = HttpResponse()
        try:
            async with self.session(basic_auth=basic_auth).request(method=str(method), url=url, **kwargs) as resp:
                self.LOG.debug(f'resp.status: {resp.status}')
                http_response.elapsed_time = float((time.monotonic() - start_ts) * 1000)
                http_response.text = await resp.text()
                if is_json(http_response.text) is True:
                    http_response.json = json.loads(http_response.text)
                    delattr(http_response, "text")
                http_response.status_code = resp.status
                self.AUDITOR.audit(f'Request: {url}', extra={
                    'request': {
                        "url": url,
                        "method": str(method),
                        "_kwargs": kwargs,
                    },
                    'response': http_response.to_dict(),
                })
                self.history.append(http_response)
                return http_response.to_dict()
        except aiohttp.ClientConnectorError as e:
            self.LOG.error(f'Connection error: {e}', exc_info=e)
        except:
            e = sys.exc_info()[0]
            self.LOG.error(f'Uncaught error: {e}', exc_info=e)

    async def get(self, *args, **kwargs):
        """
        Send an asynchronous HTTP request using the GET method.

        :param args:
        :param kwargs:
        :return:
        """
        self.LOG.debug(f'get(args={args}, kwargs={kwargs})')
        kwargs['method'] = HttpMethod.GET
        await self._fetch(**kwargs)

    async def post(self, *args, **kwargs):
        """
        Send an asynchronous HTTP request using the POST method.

        :param args:
        :param kwargs:
        :return:
        """
        self.LOG.debug(f'post(args={args}, kwargs={kwargs})')
        kwargs['method'] = HttpMethod.POST
        return await self._fetch(**kwargs)

    async def put(self, *args, **kwargs):
        """
        Send an asynchronous HTTP request using the PUT method.

        :param args:
        :param kwargs:
        :return:
        """
        self.LOG.debug(f'put(args={args}, kwargs={kwargs})')
        kwargs['method'] = HttpMethod.PUT
        return await self._fetch(**kwargs)

    async def patch(self, *args, **kwargs):
        """
        Send an asynchronous HTTP request using the PATCH method.

        :param args:
        :param kwargs:
        :return:
        """
        self.LOG.debug(f'patch(args={args}, kwargs={kwargs})')
        kwargs['method'] = HttpMethod.PATCH
        return await self._fetch(**kwargs)

    async def delete(self, *args, **kwargs):
        """
        Send an asynchronous HTTP request using the DELETE method.

        :param args:
        :param kwargs:
        :return:
        """
        self.LOG.debug(f'delete(args={args}, kwargs={kwargs})')
        kwargs['method'] = HttpMethod.DELETE
        return await self._fetch(**kwargs)

    async def options(self, *args, **kwargs):
        """
        Send an asynchronous HTTP request using the OPTIONS method.

        :param args:
        :param kwargs:
        :return:
        """
        self.LOG.debug(f'basic_auth(args={args}, kwargs={kwargs})')
        kwargs['method'] = HttpMethod.OPTIONS
        return await self._fetch(**kwargs)

    def __del__(self):
        self.loop.run_until_complete(self._connector.close())
