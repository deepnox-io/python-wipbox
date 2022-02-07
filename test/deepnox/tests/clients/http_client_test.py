#!/usr/bin/env python3

"""
Module: deepnox.tests.clients.http_client_test

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
from deepnox.clients.http_client import HttpClient
from deepnox.helpers.testing_helpers import BaseAsyncTestCase

import unittest

from deepnox.network import Scheme
from deepnox.network.http import HttpRequest, HttpMethod
from deepnox.network.urls import Url


class HttpClientTestCase(BaseAsyncTestCase):
    """
    Unit tests for :class:`deepnox.clients.http_client.HttpClient`
    """

    def test__create_a_simple_valid_instance_should_be_okay(self):
        self.assertIsInstance(HttpClient(), HttpClient)

    def test__session(self):
        client = HttpClient()
        self.assertIsInstance(client, HttpClient)

    # def test__request(self):
    #     client = HttpClient()
    #     url = Url(scheme=Scheme.HTTPS, hostname="example.org", path="/api")
    #     req = HttpRequest(method=HttpMethod.GET, url=url)
    #     self.loop.run_until_complete(client.request(req))


if __name__ == '__main__':
    unittest.main()
