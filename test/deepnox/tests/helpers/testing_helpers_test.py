#!/usr/bin/env python3

"""
Module: deepnox.tests.helpers.testing_helpers_test

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

import unittest
from types import MethodType

from deepnox.helpers.testing_helpers import BaseTestCase


class BaseTestCaseTestCase(BaseTestCase):
    def test___init__(self):
        base = BaseTestCase()
        self.assertIsInstance(base, BaseTestCase)
        attr = getattr(base, "assertNotRaises")
        self.assertIsNotNone(attr)
        self.assertIsInstance(attr, MethodType)



if __name__ == '__main__':
    unittest.main()
