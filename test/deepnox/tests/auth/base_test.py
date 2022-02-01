#!/usr/bin/env python3

"""
Module: deepnox.tests.auth.base

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
import unittest

import aiohttp

from deepnox.auth.base import BaseAuthorization
from deepnox.helpers.testing_helpers import BaseTestCase


class BaseAuthorizationTestCase(BaseTestCase):
    """
    Tests: BaseAuthorization
    """

    def test__create_valid_instance_should_be_okay(self):
        self.assertIsInstance(BaseAuthorization(), BaseAuthorization)

if __name__ == '__main__':
    unittest.main()
