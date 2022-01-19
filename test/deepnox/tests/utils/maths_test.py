#!/usr/bin/env python3

"""
Unit tests of: deepnox.utils.maths

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""

import logging
import unittest

from deepnox import loggers
from deepnox.utils.audit import timeit
from deepnox.utils.maths import percentage


class MathsUtilsTestCase(unittest.TestCase):
    """
    Mathematics utilities unit tests.
    """

    def test_percentage(self):
        self.assertEqual(4*100/12, percentage(4, 12))
        self.assertRaises(ZeroDivisionError, lambda: percentage(4, 0))


if __name__ == '__main__':
    unittest.main()
