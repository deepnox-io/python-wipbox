#!/usr/bin/env python3

"""
Module: deepnox.tests.auth.base

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
import unittest

import aiohttp

from deepnox.auth.base import BaseAuthorization, BasicAuthorization
from deepnox.helpers.testing_helpers import BaseTestCase


class BaseAuthorizationTestCase(BaseTestCase):
    """
    Tests: BaseAuthorization
    """

    def test__create_valid_instance_should_be_okay(self):
        self.assertIsInstance(BaseAuthorization(), BaseAuthorization)

    def test__check_internal_authorization(self):
        auth = BaseAuthorization()
        self.assertRaises(NotImplementedError, lambda: auth.instance)


class BasicAuthorizationTestCase(BaseTestCase):
    """
    Tests: BasicAuthorization
    """

    def test__create_valid_instance_should_be_okay(self):
        self.assertIsInstance(BasicAuthorization(username="username_test", password="password_test"),
                              BasicAuthorization)

    def test__create_instance_then_check_properties(self):
        auth = BasicAuthorization(username="username_test", password="password_test")
        self.assertEqual("username_test", auth.username)
        self.assertEqual("password_test", auth.password)
        self.assertEqual("latin1", auth.encoding)
        self.assertIsInstance(auth.instance, aiohttp.BasicAuth)


if __name__ == '__main__':
    unittest.main()
