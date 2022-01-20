#!/usr/bin/env python3

"""

Unit tests: deepnox.third.__init__

This file is a part of deepnox-box-in-progress project.

(c) 2021, Deepnox SAS.
"""
import os
import sys
import unittest

import arrow

# Very important to run unit test in JetBrains PyCharm or Idea...
from deepnox.helpers.testing_helpers import BaseTestCase

sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "src")
)
sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "test")
)


class ThirdImportTestCase(BaseTestCase):
    """
    Tests for included external librairies.
    """

    def test_import_aiohttp_dependency(self):
        self.assertNotRaises(ModuleNotFoundError, lambda: __import__("deepnox.third"))
        self.assertTrue(lambda: hasattr(__import__("deepnox.third"), "aiohttp"))

    def test_import_arrow_dependency(self):
        self.assertNotRaises(ModuleNotFoundError, lambda: __import__("deepnox.third"))
        self.assertTrue(lambda: hasattr(__import__("deepnox.third"), "arrow"))

    def test_import_jinja2_dependency(self):
        self.assertNotRaises(ModuleNotFoundError, lambda: __import__("deepnox.third"))
        self.assertTrue(lambda: hasattr(__import__("deepnox.third"), "jinja2"))

    def test_import_numpy_dependency(self):
        self.assertNotRaises(ModuleNotFoundError, lambda: __import__("deepnox.third"))
        self.assertTrue(lambda: hasattr(__import__("deepnox.third"), "numpy"))

    def test_import_pandas_dependency(self):
        self.assertNotRaises(ModuleNotFoundError, lambda: __import__("deepnox.third"))
        self.assertTrue(lambda: hasattr(__import__("deepnox.third"), "pandas"))

    def test_import_pydantic_dependency(self):
        self.assertNotRaises(ModuleNotFoundError, lambda: __import__("deepnox.third"))
        self.assertTrue(lambda: hasattr(__import__("deepnox.third"), "pydantic"))

    def test_import_requests_dependency(self):
        self.assertNotRaises(ModuleNotFoundError, lambda: __import__("deepnox.third"))
        self.assertTrue(lambda: hasattr(__import__("deepnox.third"), "requests"))

    def test_import_yaml_dependency(self):
        self.assertNotRaises(ModuleNotFoundError, lambda: __import__("deepnox.third"))
        self.assertTrue(lambda: hasattr(__import__("deepnox.third"), "yaml"))


if __name__ == '__main__':
    unittest.main()
