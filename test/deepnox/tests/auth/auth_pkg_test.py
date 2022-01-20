#!/usr/bin/env python3

"""
Module: deepnox.auth.auth_pkg_test

This file is a part of python-deepnox-box-in-progress project.

(c) 2021, Deepnox SAS.
"""

import unittest

from deepnox.helpers.testing_helpers import BaseTestCase


class AioboxPackageTestCase(BaseTestCase):
    def test__import_main_package(self):
        self.assertNotRaises(ImportError, lambda: __import__("deepnox.auth"))

if __name__ == '__main__':
    unittest.main()
