#!/usr/bin/env python3

"""
Module: deepnox.files.files_pkg_test

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

import unittest

from deepnox.helpers.testing_helpers import BaseTestCase


class AioboxPackageTestCase(BaseTestCase):
    def test_import_main_package(self):
        self.assertNotRaises(ImportError, lambda: __import__("deepnox.files"))



if __name__ == '__main__':
    unittest.main()
