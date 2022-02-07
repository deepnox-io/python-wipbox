#!/usr/bin/env python3

"""
Module: deepnox.aiorest.client

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

import asyncio
import inspect
import sys
from typing import Dict, Tuple, Type, Union

from aiohttp import ClientSession

from deepnox import loggers
from deepnox.auth.credentials import AuthorizationType, Credentials
from deepnox.aiorest.resources import Resource
from deepnox.network import Scheme
from deepnox.network.urls import Url
from deepnox.utils.maps import CannotConvertToMapTypeError, Map, to_map
from deepnox.utils.metacls import get_attributes_by_type

LOGGER = loggers.factory(__name__)
""" The module LOGGER. """

loggers.setup()


class SessionArgsBuilder(object):
    def __init__(self, o):
        self._obj = o
        self._args = {'loop': o.loop}
        self.add_basic_auth()

    def get(self):
        return self._args

    def add_basic_auth(self):
        if (
                isinstance(self._obj.credentials, AuthorizationType.BASIC_AUTH)
                is True
        ):
            self._args['auth'] = self._obj.credentials.get()
        return self


class BaseRestClient(object):
    """
    The base class from which the :class:`deepnox.aiorest.client.RestClient` class.
    """

    def __init__(
            self,
            base_url: Url,
            loop: asyncio.AbstractEventLoop = None,
            credentials: Tuple[Credentials] = None,
            connector_options: Type[Union[Dict, Map]] = None,
            base_http_headers: Type[Union[Dict, Map]] = None,
    ):
        for k in self._resources.keys():
            self._resources[k].client = self

        self.base_url = base_url
        self.loop = loop or asyncio.get_event_loop()
        self.credentials = credentials
        self.connector = to_map(connector_options)
        self.base_http_headers = to_map(base_http_headers)
        self._session = None

    async def session(self, **kwargs):
        self._session = ClientSession(**SessionArgsBuilder(self).get())
        return self._session

    def __getattribute__(self, item: str) -> Resource:
        if isinstance(item, Resource):
            return self._resources[item]
        return super().__getattribute__(item)


class RestClientMetaClass(type):
    """
    The metaclass to simplify declaration of resources list.
    """

    LOG = LOGGER.getChild('RestClientMetaclass')
    """ The metaclass LOGGER. """

    def __init__(self, what, bases=None, dict=None):
        print('dict', dict)
        for k in inspect.getmembers(bases[0]):
            print('member =', k)


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
        print('clsname, bases, attrs', clsname, bases, attrs.items())


        new_attrs['_resources'] = {}  #
        for k, v in attrs.items():
            print('k, v == ', k, v)
        return super().__new__(
            mcs, clsname, bases, new_attrs
        )




class RestClient(BaseRestClient, metaclass=RestClientMetaClass):

    def __init__(
            self,
            base_url: Url,
            loop: asyncio.AbstractEventLoop = None,
            credentials: Tuple[Credentials] = None,
            connector_options: Type[Union[Dict, Map]] = None,
            base_http_headers: Type[Union[Dict, Map]] = None,
    ):
        super().__init__(base_url,
                         loop,
                         credentials,
                         connector_options,
                         base_http_headers,
                         )



