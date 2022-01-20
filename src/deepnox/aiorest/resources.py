#!/usr/bin/env python3

from functools import wraps
from types import FunctionType

from deepnox import loggers
from deepnox.utils.pyutils import copy_func
from deepnox.utils.strings_utils import remove_slash_at_start_and_at_end

LOGGER = loggers.factory(__name__)
""" The module LOGGER. """


def run_as_async_request(coro):
    """
    Run a HttpRequest object as an asynchronous request.
    :param coro:
    :return:
    """
    @wraps(coro)
    async def _impl(self, *method_args, **method_kwargs):
        LOGGER.debug('request._impl wrapper', extra={'method_args': method_args,
                                                     'method_kwargs': method_kwargs})
        req = coro(self, *method_args, **method_kwargs)
        return await self._do_request(**req)
    return _impl

# def to_async(coro):
#     @wraps(coro)
#     def _impl(self, *method_args, **method_kwargs):
#         LOGGER.debug("request._impl wrapper", extra={"method_args": method_args,
#                                                      "method_kwargs": method_kwargs})
#         req = coro(self, *method_args, **method_kwargs)
#
#         return self._do_request(**req)
#
#     return _impl

class ResourceMetaClass(type):
    """
    The metaclass used to create derived {Resource} class.
    """

    LOG = LOGGER.getChild('ResourceMetaClass')
    """ The metaclass LOGGER. """

    _instances = {}
    """ A {dict} containing :class:`deepnox.aiorest.resources.Resource` objects which must be a singleton. """

    def __new__(mcs, clsname, bases, attrs):
        """
        __new__

        :param clsname:
        :param bases:
        :param attrs:
        """
        mcs.LOG.debug(f'__new____new__(mcs, clsname, bases, attrs)', extra={'_mcs': mcs,
                                                                      '_clsname': clsname,
                                                                      '_bases': bases,
                                                                      '_attrs': attrs,})
        print({'_mcs': mcs,
               '_clsname': clsname,
               '_bases': bases,
               '_attrs': attrs,})
        new_attrs = attrs
        new_attrs['_attrs'] = {}
        new_attrs['_request_builders'] = {}
        new_attrs['_endpoints'] = {}

        for k, v in attrs.items():
            if type(v) == str and k in ['name', 'prefix']:
                new_attrs['_attrs'][k] = v
            elif isinstance(v, FunctionType) and not v.__name__.startswith('__') and not v.__name__.endswith('__'):
                new_attrs['_request_builders'][k] = copy_func(v)
                new_attrs['_endpoints'][k] = None  # Will be defined at __call__

            # new_attrs['_request_builders'][k] = v

        return super(ResourceMetaClass, mcs).__new__(mcs, clsname, bases, new_attrs)

    def __call__(self, *args, **kwargs):
        self.LOG.debug('__call__(cls, *args, **kwargs', extra={'_self':self, '_args': args, '_kwargs': kwargs})
        obj = self.__new__(self, *args, **kwargs)
        obj.__init__(*args, **kwargs)
        print('obj.client', obj.client, list(self._endpoints.keys()))
        for request_builder_name in self._endpoints.keys():
            request_builder_fn = self._request_builders.get(request_builder_name)
            # setattr(self, f"_{request_builder_name}_request_builder", request_builder_fn)
            return request_builder_fn(obj, *args, **kwargs)
        return obj




class Resource(object, metaclass=ResourceMetaClass):
    """
    The base class to define {Resource}
    """

    LOG = LOGGER.getChild('Resource')
    """ The LOGGER. """

    def __init__(self, **kwargs):
        self.LOG.debug('__init__(self, **kwargs)', extra={'kwargs': kwargs})
        self.client = kwargs.get('client')

    async def _do_request(self, **req):
        self.LOG.debug('_do_request(self, req)', extra={'req': req})
        x = await self.client._fetch(**req)
        return x

    def absolute_endpoint_url(self, url: str = None):
        """
        Returns absolute URL of endpoint.

        :param url: The relative URL of service.
        :return: The absolute URL of endpoint.
        :rtype: str
        """
        print('1')
        self.LOG.debug('absolute_endpoint_url(self, url: str = None)', extra={'url': url})
        url = url if url is not None and type(url) == str and len(url) > 0 else ''
        print('2')

        r = '/'.join([remove_slash_at_start_and_at_end(str(self.client.base_url)),
         remove_slash_at_start_and_at_end(self._attrs['prefix']),
         remove_slash_at_start_and_at_end(url)])
        return r

    def headers(self, d: dict = None):
        """
        Returns HTTP headers for request.

        :param d: The HTTP headers.
        :type d: dict
        :return: The final HTTP headers (updated using common base headers).
        :rtype: dict
        """
        if d is None:
            d = {}
        d.update(self.client._common_headers)
        if self.bearer_token is not None:
            d.update({'Authorization': 'Bearer {self.bearer_token}'})
        return d
