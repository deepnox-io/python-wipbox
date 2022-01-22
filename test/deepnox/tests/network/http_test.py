#!/usr/bin/env python3

"""
Module: deepnox.tests.network.http_test

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
import logging
import unittest

from deepnox.helpers.testing_helpers import BaseTestCase
from deepnox.network import Scheme
from deepnox.network.http import HttpRequest, HttpMethod, HttpGetRequest, HttpPutRequest, HttpPostRequest, \
    HttpPatchRequest, HttpOptionsRequest, HttpDeleteRequest
from deepnox.network.urls import Url

LOGGER = logging.getLogger(__name__)
""" The main LOGGER. """




class HttpMethodTestCase(unittest.TestCase):
    """
    Test cases for :class:`deepnox.network.http.HttpMethod`
    """

    def test_create_instance_without_positional_argument_should_raise_type_error(self):
        self.assertRaises(TypeError, lambda: HttpMethod())

    def test_create_instance_with_non_existing_item_should_raise_value_error(self):
        self.assertRaises(ValueError, lambda: HttpMethod("fake_method"))

    def test_create_instance_with_existing_item_should_be_okay(self):
        self.assertIsInstance(HttpMethod("get"), HttpMethod)
        self.assertIsInstance(HttpMethod("post"), HttpMethod)
        self.assertIsInstance(HttpMethod("put"), HttpMethod)
        self.assertIsInstance(HttpMethod("options"), HttpMethod)
        self.assertIsInstance(HttpMethod("head"), HttpMethod)
        self.assertIsInstance(HttpMethod("patch"), HttpMethod)

    def test_creating_an_instance_with_an_existing_but_badly_spelled_parameter_should_be_ok(self):
        self.assertIsInstance(HttpMethod("Get"), HttpMethod)
        self.assertIsInstance(HttpMethod("pOst"), HttpMethod)
        self.assertIsInstance(HttpMethod("pUt"), HttpMethod)
        self.assertIsInstance(HttpMethod("optIONS"), HttpMethod)
        self.assertIsInstance(HttpMethod("heAD"), HttpMethod)
        self.assertIsInstance(HttpMethod("PatCH"), HttpMethod)

    def test_value_of_each_http_method_should_be_okay(self):
        self.assertEqual(HttpMethod.GET.value, "get")
        self.assertEqual(HttpMethod.POST.value, "post")
        self.assertEqual(HttpMethod.PUT.value, "put")
        self.assertEqual(HttpMethod.OPTIONS.value, "options")
        self.assertEqual(HttpMethod.HEAD.value, "head")


class HttpRequestTestCase(BaseTestCase):
    """
    Test cases of :class:`deepnox.network.http.HttpRequest`
    """

    def test__get_method_func_from_client(self):
        url = Url(scheme=Scheme.HTTPS, host="example.org", path="api/test")
        req = HttpRequest(url=url)
        self.assertIsNotNone(req)


class HttpGetRequestTestCase(unittest.TestCase):
    """
    Test cases of :class:`deepnox.network.http.HttpGetRequest`
    """

    def test__create_a_valid_instance_should_be_okay(self):
        url = Url(scheme=Scheme.HTTPS, host="example.org", path="api/test")
        req = HttpGetRequest(url=url)
        self.assertEqual(HttpMethod.GET, req.method)


class HttpPostRequestTestCase(unittest.TestCase):
    """
    Test cases of :class:`deepnox.network.http.HttpPostRequest`
    """

    def test__create_a_valid_instance_should_be_okay(self):
        url = Url(scheme=Scheme.HTTPS, host="example.org", path="api/test")
        req = HttpPostRequest(url=url)
        self.assertEqual(HttpMethod.POST, req.method)


class HttpPutRequestTestCase(unittest.TestCase):
    """
    Test cases of :class:`deepnox.network.http.HttpPutRequest`
    """

    def test__create_a_valid_instance_should_be_okay(self):
        url = Url(scheme=Scheme.HTTPS, host="example.org", path="api/test")
        req = HttpPutRequest(url=url)
        self.assertEqual(HttpMethod.PUT, req.method)


class HttpPatchRequestTestCase(unittest.TestCase):
    """
    Test cases of :class:`deepnox.network.http.HttpPutRequest`
    """

    def test__create_a_valid_instance_should_be_okay(self):
        url = Url(scheme=Scheme.HTTPS, host="example.org", path="api/test")
        req = HttpPatchRequest(url=url)
        self.assertEqual(HttpMethod.PATCH, req.method)


class HttpPatchOptionsTestCase(unittest.TestCase):
    """
    Test cases of :class:`deepnox.network.http.HttpPutRequest`
    """

    def test__create_a_valid_instance_should_be_okay(self):
        url = Url(scheme=Scheme.HTTPS, host="example.org", path="api/test")
        req = HttpOptionsRequest(url=url)
        self.assertEqual(HttpMethod.OPTIONS, req.method)


class HttpDeleteOptionsTestCase(unittest.TestCase):
    """
    Test cases of :class:`deepnox.network.http.HttpPutRequest`
    """

    def test__create_a_valid_instance_should_be_okay(self):
        url = Url(scheme=Scheme.HTTPS, host="example.org", path="api/test")
        req = HttpDeleteRequest(url=url)
        self.assertEqual(HttpMethod.DELETE, req.method)


if __name__ == "__main__":
    unittest.main()
